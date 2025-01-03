FROM public.ecr.aws/lambda/python:3.12

WORKDIR ${LAMBDA_TASK_ROOT}

# 필요한 파일 복사
COPY requirements.txt .
COPY main.py .

# 의존성 설치
RUN pip install -r requirements.txt

# Lambda 핸들러 설정
CMD [ "lambda_function.handler" ]