import json
import random
import base64

def lambda_handler(event, context):
    # 포츈 쿠키 메시지 리스트
    fortune_messages = [
        "당신의 미래는 밝습니다.",
        "오늘은 새로운 시작의 날입니다.",
        "곧 좋은 소식을 듣게 될 것입니다.",
        "당신의 노력이 곧 결실을 맺을 것입니다.",
        "인내는 쓰지만 그 열매는 달콤할 것입니다.",
        "당신의 꿈을 향해 한 걸음 더 나아가세요.",
        "작은 친절이 큰 변화를 만들 것입니다.",
        "오늘 하루 웃음 가득한 하루 되세요.",
        "당신의 창의력이 빛을 발할 때입니다.",
        "새로운 만남이 당신의 인생을 바꿀 것입니다.",
        "도전을 두려워하지 마세요. 그것이 당신을 성장시킬 것입니다.",
        "당신의 직감을 믿으세요. 그것이 당신을 옳은 길로 인도할 것입니다.",
        "오늘 하루 감사한 마음으로 시작하세요.",
        "당신의 열정이 성공의 열쇠가 될 것입니다.",
        "작은 변화가 큰 결과를 만들어낼 것입니다.",
        "당신의 긍정적인 태도가 주변 사람들에게 영감을 줄 것입니다.",
        "오늘은 당신의 재능을 발견하는 날이 될 것입니다.",
        "어제의 실수는 오늘의 교훈이 됩니다.",
        "당신의 꿈을 포기하지 마세요. 그것은 이루어질 것입니다.",
        "새로운 기회가 당신을 기다리고 있습니다.",
        "당신의 미소가 누군가의 하루를 밝게 만들 것입니다.",
        "오늘 하루 당신이 행복할 이유를 찾아보세요.",
        "당신의 독특함이 당신의 강점입니다.",
        "어려움은 당신을 더 강하게 만들 것입니다.",
        "당신의 친절한 행동이 세상을 바꿀 수 있습니다.",
        "오늘은 당신의 재능을 나누는 날입니다.",
        "당신의 열정을 따르세요. 그것이 당신을 성공으로 이끌 것입니다.",
        "작은 진전도 여전히 진전입니다. 계속 나아가세요.",
        "당신의 노력이 곧 인정받을 것입니다.",
        "오늘 하루 새로운 것을 배워보세요."
    ]
    
    # 랜덤 메시지 선택
    random_message = random.choice(fortune_messages)
    
    # 파일 내용 생성 및 base64 인코딩
    file_content = random_message.encode('utf-8')
    file_content_base64 = base64.b64encode(file_content).decode('utf-8')
    
    # Lambda 함수 응답 생성
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain',
            'Content-Disposition': 'attachment; filename=fortune_cookie.txt'
        },
        'body': file_content_base64,
        'isBase64Encoded': True
    }
    
    return response
