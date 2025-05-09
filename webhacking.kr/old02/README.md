- cookie의 time값을 조작하여 blind sqli를 수행하여 password를 알아내는 문제이다.
  
- (SELECT count(table_name) FROM information_schema.tables 
 WHERE table_schema = database())
  - 여기서 information_schema.tables는 현재 DB서버에 존재하는 모든 테이블에 관한 메타데이터를 담고있는 시스템 테이블이다.
  - table_schema = database()는 현재 use database; 로 접속한 사용중인 데이터베이스의 테이블만을 의미한다.
  - table_name은 각 테이블의 이름이다.

- (SELECT length(table_name) FROM information_schema.tables 
 WHERE table_schema = database() 
 limit 0, 1)
  - 여기서는 table_name의 길이를 가져온다.
  - 테이블 갯수마다 결과가 반환될텐데 앞서 2개인걸 확인했으니 2개의 결과가 나올것이다
  - 그래서 limit 0 offset 1 을 통해 2개중 첫번째걸 가져온다.(13)
  - limit 1,1은 두번째꺼 (3)

- (SELECT ascii(substring(table_name,1,1)) FROM information_schema.tables 
 WHERE table_schema = database() 
 limit 1, 1)
   - 2번째꺼는 한글자씩 ascii값을 확인해보니 각각 108, 111, 103이 나왔다.
   - 1번째 꺼는 admin_area_pw
 
 - (SELECT count(column_name) FROM information_schema.columns WHERE table_name = 'admin_area_pw')
   - column_name
   - information_schema.columns 에서 찾는다.
   - 답은 1이 나왔다. 컬럼이 하나밖에 없는 것.
  
 - 이 컬럼의 이름은 앞선 방법을 이용해 pw인걸 알 수 있다.
 - 마지막으로 admin_area_pw라는 table안의, pw라는 column내용을 읽어주면 답을 구할 수 있다!