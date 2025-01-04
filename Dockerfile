FROM public.ecr.aws/lambda/python:3.12

WORKDIR ${LAMBDA_TASK_ROOT}

# 필요한 파일 복사
COPY requirements.txt .

# Lambda 핸들러 설정
CMD [ "main.lambda_handler" ]
