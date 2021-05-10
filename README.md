### 실행 환경 (Preferences : Project Interpreter 참고)
    + Python 3.7 version
    
    + 코드 실행에 필요한 라이브러리 목록 (requirements.txt 파일 참고)
        # pip3 리스트 확인
        
            $ pip3 list
            
        # requirements.txt 파일 생성하기
        
            $ pip3 freeze > requirements.txt
        
        # requirements.txt 파일에 freeze 된 list들 install 하기
            
            $ pip3 install -r requirements.txt
            
# xgboost 설치
    - 설치 관련 참고 링크 : 
        1. https://stackoverflow.com/questions/57483499/how-to-install-xgboost-on-macos
    
    - 설치 과정             
    # macOS 환경에서는 다음 과정이 필요함
    ------------------------------------------------------------
    $ brew install libomp
    ------------------------------------------------------------
    $ brew instasll cmake
    $ cmake --version
    
    $ git clone --recursive https://github.com/dmlc/xgboost.git
    $ cd xgboost
    $ mkdir build
    $ cd build
    $ cmake ..
    $ make -j4
    
    $ cd ../python-package
    $ pip3 install -e .
      
# xgboost 예측모형 관련 설명
    - xgboost 예측모형 관련 참고 링크 :       
      1. https://statkclee.github.io/model/model-python-xgboost-hyper.html