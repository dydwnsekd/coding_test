from PIL import Image, ImageDraw, ImageFont
import imageio
import numpy as np

# === 설정 ===
text_sequence = ["테", "스", "트", "용" ,"👍"]
image_size = (128, 128)
font_size = 128
bg_color = "black"
text_color = "white"
frame_duration = 300  # ms
loop = 0 # 반복 횟수
font_path = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
emoji_image_path = "thumbs_up.png"
output_path = "slack_emoji_test.gif"

# === 글자 위치 계산 함수 ===
def get_text_position(draw, text, font, image_size):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    return ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)

# === 폰트 로드 ===
font = ImageFont.truetype(font_path, font_size)

# === 엄지척 이미지 불러오기 및 크기 조절 ===
thumbs_up_img = Image.open(emoji_image_path).convert("RGBA")
thumbs_up_img = thumbs_up_img.resize((64, 64), Image.Resampling.LANCZOS)

# === 프레임 생성 ===
frames = []

for i, text in enumerate(text_sequence):
    base_img = Image.new("RGBA", image_size, color=bg_color)
    draw = ImageDraw.Draw(base_img)

    if i < len(text_sequence) - 1:
        # 텍스트 프레임
        pos = get_text_position(draw, text, font, image_size)
        draw.text(pos, text, fill=text_color, font=font)
    else:
        # 마지막 프레임은 이모지 이미지 삽입
        emoji_pos = (
            (image_size[0] - thumbs_up_img.width) // 2,
            (image_size[1] - thumbs_up_img.height) // 2
        )
        base_img.paste(thumbs_up_img, emoji_pos, thumbs_up_img)

    frames.append(np.array(base_img.convert("RGB")))

# === GIF 저장 ===
imageio.mimsave(output_path, frames, format="GIF", duration=frame_duration, loop=loop)
print(f"완성된 GIF 저장됨: {output_path}")
