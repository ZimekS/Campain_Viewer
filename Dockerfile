FROM python:3
 
ENV APP /app/Campain_Viewer
 
WORKDIR $APP
 
COPY main.py .
COPY website/ ./website/
#RUN  python3 -m venv env
#RUN  env/activate.sh && pip3 install flask 
RUN pip3 install flask && pip3 install Flask-SQLAlchemy
CMD ["flask", "--app=main.py", "run", "--host=0.0.0.0", "--port=8080"]