import base64
import random
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont


class Captcha(object):
    # 图片的宽度和高度
    size = (130, 48)
    # 字体大小
    fontsize = 28
    # 干扰线条数
    line_number = 3

    @classmethod
    def __gen_line(cls, draw, width, height):
        begin = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([begin, end], fill=cls.__gen_random_color(80, 200), width=2)

    @classmethod
    def __gen_random_color(cls, start=255, end=255):
        random.seed()
        return (
            random.randint(start, end),
            random.randint(start, end),
            random.randint(start, end),
        )

    @classmethod
    def __gen_points(cls, draw, point_chance, width, height):
        chance = min(100, max(0, int(point_chance)))
        for w in range(width):
            for h in range(height):
                temp = random.randint(0, 100)
                if temp > 100 - chance:
                    draw.point((w, h), fill=cls.__gen_random_color(50, 200))

    @classmethod
    def __gen_random_font(cls):
        fonts = ["msyhbd.ttf"]
        font = random.choice(fonts)
        return "./static/fonts/" + font

    @classmethod
    def gen_code(cls):
        num1 = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        num2 = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        operator = random.choice(['+', '-', '*'])
        if operator == "+":
            text = str(num1) + " + " + str(num2) + " = ?"
            code = num1 + num2
        elif operator == "-":
            text = str(num1) + " - " + str(num2) + " = ?"
            code = num1 - num2
        else:
            text = str(num1) + " × " + str(num2) + " = ?"
            code = num1 * num2
        return text, code

    @classmethod
    def gen_base64(cls):
        code, image = cls.gen_graph_captcha()
        buffer = BytesIO()
        image.save(buffer, "PNG")
        buf_bytes = buffer.getvalue()
        base64_data = 'data:image/png;base64,' + str(base64.b64encode(buf_bytes), 'utf-8')
        return code, base64_data

    @classmethod
    def gen_graph_captcha(cls):
        width, height = cls.size
        # A表示透明度
        image = Image.new("RGBA", (width, height), cls.__gen_random_color())
        # 字体
        font = ImageFont.truetype(cls.__gen_random_font(), cls.fontsize)
        # 创建画笔
        draw = ImageDraw.Draw(image)
        # 生成随机字符串
        text, code = cls.gen_code()
        # 字体大小
        font_width, font_height = font.getsize(text)
        # 填充字符串
        draw.text(
            ((width - font_width) / 2, (height - font_height) / 2 - 2),
            text,
            font=font,
            fill=cls.__gen_random_color(10, 200),
        )
        # 绘制干扰线
        for x in range(0, cls.line_number):
            cls.__gen_line(draw, width, height)
        # 绘制噪点
        cls.__gen_points(draw, 1, width, height)
        return code, image
