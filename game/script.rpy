﻿# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define uk = Character('???', color="#c8ffc8")
define sh = Character('나', color="#c8ffc8") #효설하
define ju = Character('하지은', color="#c8ffc8")
define jh = Character('하지현', color="#c8ffc8")
define tg = Character('2층 여자아이', color="#c8ffc8")
# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False

# 여기에서부터 게임이 시작합니다.
label start:

    scene bg black
    with fade

    "Prologue - 방향"
    
    "왜 살고 있는지는 모른다."
    "다만, 내가 살아있다, 라는 걸 느꼈을 때는 모든 게 너무 늦어있었다."
    "정확히 언제부터인지는 모른다."
    "다만, 날 가르친 스승이 죽었다는 걸 뒤늦게 알았을 때, 분명히 그 이후였다."
    "앞으로는 어떻게 해야 할 지 모른다."
    "다만, 내가 걷는 이 교안의 골목은 날 이끌어 줄 것이라 믿는다."
    "사람을 죽이는 건 내 일이 아니다."
    "단지, 사람을 줄이고 있을 뿐이다."

    scene bg white
    with fade

    "파괴라는 건, 새로운 것을 시작하기 위해 꼭 필요한 것이기에."
    "묵묵히 그 일을 하고 있을 뿐이다."
    "깨끗이 파괴될 수록, 더욱 새로운 세상을 만들 수 있으니까."

    scene bg 1
    with fade

    uk "듣던 것보단 많이 어린데, 정말 총을 쏠 수 있다고?"

    show sh_kid_hoodon
    with dissolve

    sh "...븅신새애끼"

    scene bg 1

    "슬럼가, 골목 안의 싸구려 술집."
    "만나자마자 잡소리부터 하길래 한번 불러봤더니, 곧장 등 뒤에서 멱살을 잡힌다."
    "얼굴에 상처가 많은 대머리 아저씨가 내 두꺼운 후드 점퍼채로 목을 붙잡아든다."
    "이런 폭행에도 변함없이 날카로운 눈으로 술집의 전등 아래에서 반짝이는 대머리를 똑바로 마주본다."
    "그러면서도 내 손에는 해머가 뒤로 당겨진 권총이 들려, 깡패의 배에 슬쩍 집어넣고 있다."
    "번들번들한 대머리를 뻘쭘하게 쓸어넘기고 아이의 목을 스르륵 놓아준다."

    show sh_kid_hoodon
    with dissolve

    sh "느 모가지는 느가 단디 챙기야댄디. 여그 땅덩이가 지똥맨큼 쫍아서리 느매겉이 큰 놈덜은 눈에 띄기가 십상이라."
    "제대로 알아듣지 못했다는 듯 눈짓을 하자 다시 테이블로 고개를 돌려 술 컵을 집어 들어 입에 털어 넣는다."
    "내가 사투리를 섞어 말하자, 주변 다른 사람들 몇몇이 의외인 듯 쳐다본다."
    sh "머칸다고 글케 쳐다보노, 내같은 늠 첨보나. 느가 느그집 대가리도 아이고, 따까리헌테꺼정 말 똑띠 해야긋나."

    scene bg 1

    "목을 졸랐던 대머리 아저씨가 나를 한참을 쳐다보다가, 저 앞에 서 있던 사람에게 시켜 검은색 배낭을 들고오게 한다."
    "책상에 무거운 가방을 내려놓았지만, 가볍게 무시하고서 손에 든 술잔을 익숙한 기술로 후드 안으로 흘려버린다."
    "대머리는 큭큭 웃으며 지퍼를 열어서 안에 가득 담긴 돈가방을 보여준다."
    "비어버린 술잔을 돈이 담긴 가방에 탁탁 털고 테이블 가운데로 밀어낸다."
    "돈뭉치 위에는 작은 사진 몇 장이 놓여있다."

    define exbald = Character('대머리', color="#ffffff") #엑스트라는 그때그때 ex(엑스트라)를 붙여 지정한다.

    exbald "얼마 전 지중에 들어간 남자 셋 중의 한 명이 나머지 둘을 죽이고 이 근처까지 와서 깽판을 치고 있다. 우리가 해도 되지만, 최근에 뒤숭숭한 일들이 많으니까 두 명은 군인 출신에-"

    show sh_kid_hoodon
    with dissolve

    sh "그만. 글케가 내 가가 가를 죽이삐라꼬? 긂, 어애 죽여주까."
    "대머리는 살짝 고개를 내밀고 입술을 과장되게 씰룩거리며 말한다."
    exbald "잔인하게 죽여서, 전시해. 네 특기잖아."
    sh "하! 거 참말로 사람 볼 줄 아노. 죽은 느그 아들이 그르디?"
    "대머리는 죽은 동료들을 아무렇지 않게 말하는 아이에게 화가 치밀지만, 여전히 자신의 배에 박혀있는 총구에 차갑게 식는다."
    sh "오케 금 금마만 싹! 하고 내는 간다. 원래 나가 돈은, 그 머고, 비대면으로만 받는디, 가방 째로 준다이께 함 봤다."
    exbald "기왕 돈 받아갈 거 후드만 내려봐 주지?"
    sh "돈은 느그 읎어도 천지삐까린디 내 와 그러간디?"

    scene bg black
    with fade

    "말은 그렇게 해도 가방을 챙겨들고 등에 들쳐 매면서 후드를 살짝 뒤로 내린다."
    "새카만 가면 뒤로는 갈색 긴 머리를 여러 번 묶어서 후드 안에 숨기고 있었다."
    "긴 장발을 올려 말아, 얇은 목선이 드러날 정도로 당겨진 머리카락 아래로는 얼굴과 표정이 이마부터 턱까지 가리는 가면에 덮여있다."
    "검은 마스크에 더 검은 매직으로 웃는 입만 그려져 있는 가면."
    "그 아래로는 평범한 점퍼와 짧은 치마 두 겹과 왼쪽 다리만 감싸는 검은 스타킹이 내려온다."

    scene bg white
    with fade
    
    "chapter 1 - 산전수전"

    "1편 - 바보자슥"

    "지중은 그렇게 큰 조직은 아니다."
    "기껏해야 거리 한두 블록 점거하고 밤낮으로 술이나 까던 사람들이었는데."
    "최근에는 원래 살던 거리를 나와 조금씩 밖으로 영향을 확대해나가는 게 다른 상대들에게는 안 좋게 보였을 것이다."
     
    scene bg 1
    show sh_kid_hoodon
    with dissolve

    sh "그어억-. 왜 아제들은 술 겉은걸 좋타카는겨."
 
    "거리 근처로 오자, 이니 한 번 패싸움을 벌이고 간 흔적이 있다."
    "부러진 목각들과 도로에 널브러진 쇠파이프, 피바다와 여기저기 쓰러져있는 사람들."
    "그런 길거리를 지나는 어린아이에게 신경도 안 쓰는 듯, 문 닫은 술집 테라스에서 섹스하고 있는 두 남자와 여자 1명."
    "지중이 점거하고 있는 도로로 들어서자 밖에서 온 사람을 경계하는 시선이 여기저기서 느껴진다."
    "이미 한 번 진탕 싸움을 치른 이들이 또다시 찾아온 이에 대한 고까움은 곧 행동으로 나타났다."

    uk "너 뭐야?"
    "옆 건물에서 뛰어내린 한 여자가 이방인에게 쏘아댄다."
    "이미 주변에 많은 사람이 포진해있는 건 물론이고 확인차 나온 이 여자도 주머니에 최소 무기를 하나 이상 가지고 있는 거로 보인다."
    sh "나가 길을 좀 잘못 들어가꼬 여까지 왔는디."
    uk "말하는 꼬라지가 그게 뭐야?"
    "점퍼 주머니에 손을 푸욱 찔러 넣은 채로 비웃는 여자 앞까지 걸어가자 커다란 너클을 낀 주먹이 휙 날라온다."
    "직선으로 날아오는 주먹을 가볍게 피하고 발을 걸어 넘어뜨린다."
    sh "어메, 무시라. 근거 끼고 넘한티 글케 쓰다 고꾸라져가 디져뿐디."
    "지중의 거리를 지키러 나왔던 여자가 쓰러지자 사방의 건물에서 다른 사람들도 모두 뛰어내린다."
    "적어도 다섯에서 주변에 더 지켜보는 사람들까지 열은 넘어 보인다."
    sh "그거, 돈 가방이냐? 너 업자여?"
    uk "허허, 이 좆만이가 우리를 돼지국밥으로 아는가, 혼자 기어들어 왔으면 두 다리 분질러가 기어가야제."
    "뒤에서 험한 말을 입에 올리며 날이 많이 뭉개진 칼을 긴 목각에 묶어서 창처럼 든 사람이 앞으로 나선다."
    "바닥에 엎어졌던 여자는 다시 일어서서 한쪽 벽으로 붙었다가 저 멀리 사라진다."
    "아이는 등에 짊어 맨 가방을 툭툭 두드리며 말한다."
    sh "느그는 쌈질도 짬순으로 허나? 야가 가가? 떠오르는 태양을 떨짜달라고 이 돈을 받었는디."
    "창을 한 바퀴 크게 빙 돌리고 아이를 향해 달려든다."
    sh "퍼뜩 온나. 내도 집 가서 얼러 디비 잘란다."
    "바로 앞까지 와서 내지른 창을 슬쩍 옆으로 피하고, 치마 총을 꺼내서 가까운 얼굴에다 대고 탕 쏜다."
    "옆 통수가 날아가 머리가 반으로 쪼개지며 아이에게 달려오던 속도 그대로 바닥에 엎어진다."
    "피가 후두둑 하면서 멀리 튀고, 옆에서 지켜보던 이들도 크게 소리치며 앞뒤 가리지 않고 총을 쏜 아이에게 뛰어든다."
    uk "시발, 그 총잡이 새끼다!"
    uk "잡아! 저번에 상초를 쏴 죽인 새끼야!"
    "곧바로 뒤돌아서 내달리기 시작한 아이는 수많은 사람에게 둘러쳐져 쫓긴다."
    "뛰면서도 뒤돌아서 도발을 서슴지 않는 아이가 소리친다."
    sh "아한테 깨꼬닥 디져때요! 여개저개 들쑤고 댕기다, 쪼꼬미한테 대가리 쪼개져때요!"
    uk "거기 서라! 지금 서면 깔끔하게 죽여주마!"
    "중지를 치켜들며 코너를 돌아들어서서, 곧바로 붉은 벽돌 담장을 휙 뛰어넘는다."
    "간단히 따돌려진 지중의 갱단원들은 빈 거리를 계속 달려나간다."
    sh "빙신들, 쯧."
    "담장 아래에서 돈 가방을 꺼내서 돈을 세기 시작한다."
    "몇 분이 지나도록 손가락에 침을 발라가며 세다가 어느 순간 그만둔다."
    sh "모가지 하나 치곤 장값이 넘는디. 내 면상 하나 보겄다고 글케 돈을 쓴긴가."
    "가방에 다시 돈을 다 집어넣고 끌어안고 잠을 청한다."
    "조금 있자니 계단 삐그덕 거리는 소리가 들려 고개를 드니, 2층집 사는 여자아이가 집에 들어가고 있었다."
    "가끔 슬럼가 밖에서 마주쳤기에 가볍게 인사를 건넨다."
    sh "거 누님요. 자리 있거든 내도 재워주소."
    tg "...병신."
    "어두운 담장 아래에서 이상한 요구나 한 아이에게 욕 한마디 하고 쾅 소리 나게 문을 닫고 사라진다."

    scene black
    with fade

    "2편 - 꼭두배기"














    return