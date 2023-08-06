import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path, override=True)

from apps import create_app

# 创建应用
app = create_app()

if __name__ == '__main__':
    app.run()
