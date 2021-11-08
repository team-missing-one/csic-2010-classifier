# 국민대학교 2021 정보보호와시스템보안 머신러닝 프로젝트 1

## 팀원  
백승렬(20202086), 이윤서(20181676), 최호경(20171717), 한진교(20152868)  

## 필요 모듈  
Scikit-Learn (0.22 or higher is required)  

## 코드 별 설명  
### csic_parser.py  
CSIC 2010 원본 데이터에서 유의미한 문자열만 파싱하는 코드가 있습니다. parse() 함수를 실행하여 문자열을 파싱합니다. 그 외에도 파싱된 데이터 셋을 리스트로 불러오는 load_parsed(), scikit-learn에 내장된 데이터 셋 형태로 구조를 맞춰주는 make_data_set(), 그리고 두 데이터 셋을 결합하는 combine_data_set()이 있습니다.  

### DecisionTree.py  
결정 트리 모델로 파싱한 데이터 셋을 훈련한 결과를 출력합니다.  

### LR.py  
로지스틱 회귀 모델로 파싱한 데이터 셋을 훈련한 결과를 출력합니다.  

### RF.py  
Random Forest 모델로 파싱한 데이터 셋을 훈련한 결과를 출력합니다.  

### SVM.py  
Support Vector Machine 모델로 파싱한 데이터 셋을 훈련한 결과를 출력합니다.  

### ada.py  
AdaBoost로 파싱한 데이터 셋을 훈련한 결과를 출력합니다.

### mlp.py  
다층 신경망으로 파싱한 데이터 셋을 훈련한 결과를 출력합니다. 본 프로젝트에서는 2개의 은닉층을 이용했습니다.  

### Summary.ipynb  
위 코드들을 요약한 주피터 노트북 파일입니다. 코랩 환경에서 데이터 셋을 구글 드라이브와 연동하여 실행이 가능합니다.  

### 코드 실행  
해당 repo를 clone한 상태에서 Summary.ipynb 제외 모델 코드를 실행하면 즉시 작동하며 결과를 콘솔로 확인할 수 있습니다.  
Summary.ipynb 실행을 원하시면 코랩 환경에서 드라이브 연동 후 "/content/drive/My Drive/Colab Notebooks/infosec/proj1/" 해당 경로에 csic 폴더로 데이터 셋을 넣어 실행하면 됩니다.  
