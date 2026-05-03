FROM public.ecr.aws/lambda/python:3.11

# Install system dependencies (compiler)
RUN yum install -y gcc gcc-c++ make

# Copy requirements
COPY requirements.txt .

# Upgrade pip + force binary wheels
RUN pip install --upgrade pip \
    && pip install --no-cache-dir --only-binary=:all: -r requirements.txt -t ${LAMBDA_TASK_ROOT}

# Copy app
COPY lambda/lambda_function.py ${LAMBDA_TASK_ROOT}

CMD ["lambda_function.lambda_handler"]
