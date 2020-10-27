# 팀 로고
![Logo](https://i.imgur.com/eSiVzWJ.png)

AI 기술(머신러닝)을 활용한 통합 안보 위협요소 식별 어플

# 팀 소개
## 아미렌즈 프로젝트란?
![Logo](https://i.imgur.com/xHRPFFh.png)

"아미렌즈"는 통합안보위협요소를 감지하고 신고하는 어플 제작을 목표로하는 프로젝트입니다. 위의 자료처럼 북한의 전차, 비행기, 무인기, 지뢰 등 우리나라는 안보를 위협하는 수많은 요소가 존재합니다. 그러나 일반 군인을 포함한 위협요소를 판별하는 전문적 교육을 받지 않은 인원들은 전차, 비행기들을 식별하였을때 그것의 종류가 무엇인지, 적군의 장비는 아닌지 판별한 능력이 부족하고, 판별해낸다 하더라도 오랜 시간이 걸립니다. 만약 경계근무간, 실제 전시상황 등의 중요한 상황에서 위협요소를 눈으로 보고도, 그것을 제대로 보고하지 못한다면 돌이킬 수 없는 상황이 벌어질 수도 있습니다.

그래서 저희팀은 머신러닝을 통한 학습을 통해 사진을 입력하면 바로바로 위협요소인지 판단하고 신고까지 해주는 어플을 제작하겠다는 계획을 세웠습니다. 관련 정보를 검색하고, 프로젝트를 설계하면서 많은 안보위협요소들 중 지뢰에 의한 피해가 상당하다는 것을 알게 되었고, 지뢰 식별 기능을 먼저 제작하고 이 후 다른 안보위협요소도 추가하는 것을 계획하였습니다.

## 안보위협요소 중 지뢰를 선택한 이유
![Logo](https://i.imgur.com/MlFF9ro.png)

매년 지뢰로 인한 부상,사망자가 4명씩 꾸준히 발생하고 있는 추세로 유실지뢰는 계속 군인과 민간인 모두를 위협하고 있다.

![Logo](https://i.imgur.com/MZdpkIG.png)

유실지뢰는 폭우, 태풍을 따라 이동하며 그 위치를 파악하기가 불가능하다. 따라서 One-Stop Service를 통하여 피해를 줄여보자는 취지로 지뢰 식별을 우선적으로 진행하였다.

## 프로젝트 시연 동영상
[추가예정]

## 프로젝트 발표 동영상
[![Video Label](http://i.ytimg.com/vi/UJykk1T2HlM/1.jpg)](https://youtu.be/UJykk1T2HlM)




# 개발 과정
## 1. WEBSITE & APP
### CodePen, disqus 등 다양한 오픈소스들을 활용하여 제작

![Logo](https://i.imgur.com/N8HqIFm.png)

Armylens는 5가지 페이지로 나누어져 있고 그 기능은 다음과 같습니다.

![Logo](https://i.imgur.com/YgBlcPp.png)
![Logo](https://i.imgur.com/Ik8Ix8J.png)
![Logo](https://i.imgur.com/1svJKss.png)
![Logo](https://i.imgur.com/Psgoj3V.png)
![Logo](https://i.imgur.com/BfWZBP2.png)
![Logo](https://i.imgur.com/6fz9jNe.png)
![Logo](https://i.imgur.com/ueC4jOB.png)
![Logo](https://i.imgur.com/30Ypp8s.png)

## 2. 머신러닝
### AI learning pipeline
![Logo](https://i.imgur.com/y1gfbYX.png)

머신러닝 과정은 4단계로 나누어 진행하였습니다.

![Logo](https://i.imgur.com/9vILPDt.png)

![Logo](https://i.imgur.com/aW65jAI.png)

![Logo](https://i.imgur.com/XG9lFzE.png)

![Logo](https://i.imgur.com/S3dD1Lu.png)



### 3. Armylens project  update note
-10월 12일 개발자의 실수로 branch를 지우려다가 repository를 전부 지워버려 직접 작성합니다.

2020.10.01~2020.10.05
* 파이썬으로 구글에서 각 지뢰당 100장씩 이미지 크롤링
* 파이썬으로 네이버에서 각 지뢰당 100장씩 이미지 크롤링
* 데이터 클렌징을 통해 신뢰도에 문제가 발생할 수 있다고 판단되는 이미지를 삭제
* Teachable Machine을 이용해 각 지뢰 class에 선발된 사진 90~100장을 학습
* 프로젝트 로고 제작
* 웹사이트 지뢰종류, 사고 사례 페이지 틀 제작

2020.10.06~2020.10.10
* codepen이라는 오픈소스를 활용해 이미지업로드 구현 
* Teachable Machine을 통해 학습이 완료된 머신러닝을 클라우드에 업로드
* 클라우드에 업로드 된 머신러닝을 웹과 AJAX로 연결, 요청과 응답을 받게함
* 이미지업로드 오픈소스의 형태와 메세지를 변경하여 가독성 향상
* 지뢰 식별 결과값을 내림차순 정렬하고, 기존 1.0000000[max]에서 100%[max]로 변경하여 가독성 향상
* 로딩과 식별 두 단계로 진행되던 머신러닝을 이미지가 업로드되면 자동으로 로딩과 식별기능이 작동하도록 수정

2020.10.10~2020.10.15
* 머신러닝 결과값이 제일 높은 지뢰를 선별하여, 지뢰 이름과 설명문이 출력되도록 수정
* 웹페이지의 사이즈에 맞게 조절되는 반응형 var을 제작
* 사진 클릭시 해당 링크로 리다이렉트 되도록 지뢰 종류, 사고 사례 페이지 사진에 링크 연결
* 댓글 호스팅 서비스 disqus를 이용하여 댓글기능을 구현
* 리액트 네이티브를 활용하여 웹뷰형식의 앱을 제작(expo의 도움을 받음)
* 아이콘과 스플래시 이미지를 추가
* 소셜 북 마킹 서비스 addthis를 이용하여 공유기능을 구현


2020.10.16~2020.10.20
* 웹뷰의 폭이 달라 잘려서 출력되는 오류를 해결
* 사고사례, 건의사항 페이지의 설명문을 수정하고 관련 동영상 추가
* 퀴즈제공 서비스 proprofs를 활용해 퀴즈 기능 구현 
* ppt 초안 제작
* readme 초안제작

2020.10.21~2020.10.25
* 파이썬으로 다음에서 각 지뢰당 100장씩 이미지 크롤링
* 파이썬으로 Bing에서 각 지뢰당 100장씩 이미지 크롤링
* 데이터 클렌징을 통해 신뢰도에 문제가 발생할 수 있다고 판단되는 이미지 삭제
* 각 지뢰 class에 새롭게 데이터클렌징 작업을 거쳐 선발된 사진 180~200장을 학습시켜 머신러닝의 신뢰도 향상
* 머신러닝에서 모든 class의 신뢰도 중 아무것도 60% 넘지 않을 시 지뢰가 아닌것으로 판단하는 기능 추가
(신뢰도에 관한 이슈는 데이터의 수와 강화학습으로 인해 보완이 가능할 것으로 판단)
(현재 군사자료 사용불가로 인터넷의 자료에만 의존하여 진행)

2020.10.26~2020.10.31
* 지뢰 식별창에 경찰(112), 군부대(1338)신고 기능 추가
* ppt 제작 및 수정
* read me 제작 및 수정
* 시연 영상 제작
* 발표 영상 제작


## 기능 설계

### Data architecture
![Logo](https://i.imgur.com/xZJrRoq.png)

## 컴퓨터 구성 / 필수 조건 안내 (Prerequisites)
사용 기술
* python 3.8
* react native
* visual studio code
* ECMAScript 6 지원 브라우저 사용
* 권장: Google Chrome 버젼 77 이상

## 기술 스택 (Technique Used)
![Logo](https://i.imgur.com/z1i7GQo.png)

## 설치 안내 (Installation Process)
```bash
$ git clone git주소
$ yarn or npm install
$ yarn start or npm run start
```
 
## 팀 정보 (Team Information)
- Park jun su(starkingstar@naver.com), Github Id: starkingstar@naver.com
- You gun woo(pix_online@naver.com), Github Id: pix_online@naver.com

## 저작권 및 사용권 정보 (Copyleft / End User License)
 * [Codepen](https://github.com/osamhack2020/web_armylens_armylens/blob/master/license_codepen.md)
 * [html5up](https://github.com/osamhack2020/web_armylens_armylens/blob/master/license_html5up.md)
 * [MIT](https://github.com/osam2020-WEB/Sample-ProjectName-TeamName/blob/master/license.md)
