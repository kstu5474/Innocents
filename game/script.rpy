# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define ju = Character('하지은', color="#c8ffc8")


# 여기에서부터 게임이 시작합니다.
label start:

    play music "편안5, 밤(테라리아).mp3"

    scene bg 5 test
    with fade

    show jieun
    with dissolve

    ju "이노센스 프로젝트!"

    ju "시작합니당"

    scene bg black
    with fade

    menu:
        "시작할가요?"

        "녜":
            jump yes

        "않이오":
            jump no
        
        "샍즈":
            jump sans

label no:
    "으아악!"
    "전심, 랄랄라! 도와줘!"

    return

label sans:
    show sans
    with dissolve

    "터어엉어어얼렷구나"
    return

label yes:
    "aaaaaa"
    return