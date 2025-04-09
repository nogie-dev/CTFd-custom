
USE ctfd;

-- 여기에 필요한 테이블 생성 SQL 추가
-- 예: CREATE TABLE logs (id INT AUTO_INCREMENT PRIMARY KEY, ...);
create table container_log(
	no int primary key not null,
	container_id varchar(64) not null,
	challenge_name varchar(16) not null,
	user_name varchar(16) not null,
	user_ip varchar(15) not null,
	created_at date not null
)