import pyautogui
import random
import time

pyautogui.FAILSAFE = True

def move_random_mouse(duration=10):
    end_time = time.time() + duration
    screen_width, screen_height = pyautogui.size()

    while time.time() < end_time:
        x = random.randint(0, screen_width - 1)
        y = random.randint(0, screen_height - 1)
        pyautogui.moveTo(x, y, duration=0.2)
        time.sleep(0.3)

def main():
    run_limit = 3600  # 1시간
    start_time = time.time()

    while True:
        # 종료 여부 체크
        if time.time() - start_time >= run_limit:
            print("[INFO] 1시간 경과, 프로그램 종료")
            break

        print("[INFO] 3분 대기중...")
        time.sleep(180)

        # 종료 여부 체크
        if time.time() - start_time >= run_limit:
            print("[INFO] 1시간 경과, 프로그램 종료")
            break

        print("[INFO] 마우스 랜덤 이동 시작 (10초)")
        move_random_mouse(duration=10)
        print("[INFO] 완료")

if __name__ == "__main__":
    main()