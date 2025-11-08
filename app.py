from flask import Flask, render_template_string
import random

app = Flask(__name__)

# 背景图片列表
background_images = [
    "https://cunchuyinyue.oss-cn-guangzhou.aliyuncs.com/0504a127200345da0954422b150210ed.jpg",
    "https://cunchuyinyue.oss-cn-guangzhou.aliyuncs.com/14f321ac75ccf3faf2140673ee37661c.jpg",
    "https://cunchuyinyue.oss-cn-guangzhou.aliyuncs.com/8925aae70b396cb6676f4dce2aa5ba1f.jpg",
    "https://cunchuyinyue.oss-cn-guangzhou.aliyuncs.com/822f815514a3e16a9a9b6dd5de99b885.jpg",
    "https://cunchuyinyue.oss-cn-guangzhou.aliyuncs.com/80b84c8b7672862077a401c64334da47.jpg",
    "https://cunchuyinyue.oss-cn-guangzhou.aliyuncs.com/7ee38244263a08f41e06bcf0c1950333.jpg",
    "https://cunchuyinyue.oss-cn-guangzhou.aliyuncs.com/6b5b73100d16170b8b68608bac157a28.png",
]

messages = [
    "❤️ 记得吃饭",
    "😘 天气冷了，我很想你",
    "😊 保持好心情",
    "🍚 按时吃饭",
    "❤️ 早点休息",
    "😜 别熬夜哦",
    "😊 要开心呀",
    "❤️ 想你啦",
    "😋 多吃点好吃的",
    "😊 照顾好自己",
    "😝 要幸福哦",
    "😊 每天都要快乐",
    "❤️ 记得想我",
    "😊 保持微笑",
    "❤️ 注意身体",
    "😛 要加油呀",
    "😊 一切安好",
    "❤️ 我在想你",
    "😊 天天开心",
    "❤️ 好好吃饭",
    "😚 别太累了",
    "😊 保持可爱",
    "😝 要幸福哦",
    "😊 事事顺心",
    "❤️ 想你每一天",
    "😊 快乐每一天",
    "❤️ 按时睡觉",
    "😜 别偷懒哦",
    "😊 要幸福呀",
    "❤️ 记得爱自己",
    "😋 多喝热水",
    "😊 保持乐观",
    "❤️ 我很想你",
    "😝 要努力哦",
    "😊 一切顺利",
    "❤️ 好好生活",
    "😚 别担心哦",
    "😊 幸福每一天",
    "❤️ 要开心哦",
    "😊 别忘记我",
    "😜 要幸福呀",
    "❤️ 好好爱自己",
    "😊 天天快乐",
    "❤️ 想你哦",
    "😋 多吃点",
    "😊 照顾好自己哦",
    "❤️ 别太累",
    "😝 要开心",
    "😊 陈楚滢！",
    "😊 一切都好",
    "❤️ 我在等你",
    "😊 要幸福",
    "❤️ 好好吃饭哦",
    "😚 别熬夜",
    "😊 保持开心",
    "❤️ 记得想我哦",
    "😊 天天幸福",
    "❤️ 注意身体哦",
    "😛 要加油",
    "😊 一切安好哦",
    "❤️ 我很想你哦",
    "😊 事事顺利",
    "❤️ 好好生活哦",
    "😚 别担心",
    "😊 幸福每一天哦",
    "❤️ 要开心呀",
    "😊 别忘记我哦",
    "😜 要幸福哦",
    "❤️ 好好爱自己哦",
    "😊 天天快乐哦",
    "❤️ 想你呀",
    "😋 多吃点哦",
    "😊 照顾好自己呀",
    "❤️ 别太累哦",
    "😝 要开心呀",
    "😊 一切都好呀",
    "❤️ 我在等你呀",
    "😊 要幸福呀",
    "😝 要想我呀",
    "❤️ 陈楚滢！",
]

# 生成随机颜色（优化对比度，避免过暗）
def get_random_color():
    # 确保颜色明亮，提升可读性
    r = random.randint(150, 255)
    g = random.randint(150, 255)
    b = random.randint(150, 255)
    return f'#{r:02x}{g:02x}{b:02x}'

@app.route('/')
def index():
    default_bg = random.choice(background_images)
    html = f'''
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>神秘礼物便签</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                -webkit-tap-highlight-color: transparent;
                tap-highlight-color: transparent;
            }}
            body {{
                overflow: hidden;
                height: 100vh;
                background: url('{default_bg}') no-repeat center center fixed;
                background-size: cover;
                font-family: "Microsoft YaHei", sans-serif;
                position: relative;
                transition: background-image 1s ease-in-out;
            }}
            .bg-controls {{
                position: fixed;
                top: 10px;
                right: 10px;
                z-index: 9998;
                display: flex;
                gap: 8px;
                flex-wrap: wrap;
            }}
            .bg-btn {{
                padding: 6px 10px;
                background-color: rgba(255,255,255,0.9);
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 11px;
            }}
            .popup {{
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: white;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.2);
                z-index: 9999;
                text-align: center;
                width: 85%;
                max-width: 300px;
            }}
            .popup h3 {{
                font-size: 16px;
                margin-bottom: 12px;
            }}
            .note {{
                position: absolute;
                padding: 8px 12px;
                border-radius: 8px;
                box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
                cursor: move;
                user-select: none;
                animation: bounce 0.3s ease-out;
                max-width: 60%; /* 适配移动端宽度 */
                word-break: break-all;
                font-size: 12px; /* 缩小字体 */
                line-height: 1.4;
            }}
            @keyframes bounce {{
                0% {{ transform: scale(0.5); opacity: 0; }}
                70% {{ transform: scale(1.1); }}
                100% {{ transform: scale(1); opacity: 1; }}
            }}
            button {{
                padding: 7px 14px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 14px;
            }}
        </style>
    </head>
    <body>
        <div class="bg-controls">
            <button class="bg-btn" onclick="toggleAutoSwitch()">自动切换: 开启</button>
            <button class="bg-btn" onclick="changeBackground()">手动切换</button>
        </div>

        <div class="popup" id="popup">
            <h3>你收到一份神秘礼物</h3>
            <button onclick="closePopup()">确定</button>
        </div>
        <div id="notesContainer"></div>
        <audio id="bgMusic" loop>
            <source src="https://cunchuyinyue.oss-cn-guangzhou.aliyuncs.com/ockqAalIpRIbGAVOEeAITmJLeeAa4FYGBGECAF%20%281%29.mp3" type="audio/mpeg">
            您的浏览器不支持音频播放
        </audio>

        <script>
            const bgImgs = {background_images};
            let autoSwitchInterval = null;
            let isAutoSwitch = true;

            // 优化自动切换间隔（移动端延长至8秒，避免频繁切换）
            function startAutoSwitch() {{
                const interval = /Mobile|Android|iPhone/.test(navigator.userAgent) ? 8000 : 5000;
                autoSwitchInterval = setInterval(changeBackground, interval);
            }}

            function toggleAutoSwitch() {{
                const btn = document.querySelector('.bg-btn:first-child');
                if (isAutoSwitch) {{
                    clearInterval(autoSwitchInterval);
                    btn.textContent = "自动切换: 关闭";
                }} else {{
                    startAutoSwitch();
                    btn.textContent = "自动切换: 开启";
                }}
                isAutoSwitch = !isAutoSwitch;
            }}

            function changeBackground() {{
                const randomIdx = Math.floor(Math.random() * bgImgs.length);
                document.body.style.backgroundImage = `url('${{bgImgs[randomIdx]}}')`;
            }}

            fun