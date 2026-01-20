USE Pet_hotel;  -- pet_hotel 스키마를 사용

-- 동물 주인 테이블
CREATE TABLE pet_owner(
	owner_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL,  -- 주인 이름
    email VARCHAR(255),  -- 이메일(예약시 이메일로 체크)
    phone VARCHAR(20)  -- 전화번호(예약시 문자메시지로 2중체크)
);

-- 동물 테이블을 생성
CREATE TABLE pet(
	pet_id INT PRIMARY KEY AUTO_INCREMENT,
    owner_id INT NOT NULL,
    name VARCHAR(10), -- 동물 이름
    species VARCHAR(10), -- 동물 종
    FOREIGN KEY (owner_id) REFERENCES pet_owner(owner_id)
);

-- 객실 테이블
CREATE TABLE rooms(
	room_id INT PRIMARY KEY AUTO_INCREMENT,
    roomnumber INT NOT NULL UNIQUE, -- 방 번호 고유번호로 만들어야 겹치지 않게 만들 수 있음
    roomtype VARCHAR(50),  -- 방 타입(여러가지의 방의 종류가 나올 수 있음)
    pricePerNight DECIMAL(10, 2) NOT NULL -- (하룻밤 가격)
);

-- 예약 테이블
CREATE TABLE reservation(
  reservation_id INT PRIMARY KEY AUTO_INCREMENT,
  pet_id INT NOT NULL, -- 예약된 동물 이름 id
  owner_id INT NOT NULL, -- 예약된 동물 주인 id
  room_id INT NOT NULL, -- 예약된 객실 확인하는 id
  checkInDate DATE NOT NULL,  -- 체크인 날짜 확인
  checkOutDate DATE NOT NULL,  -- 체크아웃 날짜 확인
  FOREIGN KEY (pet_id) REFERENCES pet(pet_id),
  FOREIGN KEY (owner_id) REFERENCES pet_owner(owner_id),
  FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

-- 서비스 테이블
CREATE TABLE service (
  service_id INT PRIMARY KEY AUTO_INCREMENT,
  reservation_id INT NOT NULL,  -- 예약자 id
  servicename VARCHAR(100), -- 예약 가능한 혹은 가능한 서비스 이름
  serviceprice DECIMAL(10, 2) NOT NULL,  -- 서비스 가격
  FOREIGN KEY (reservation_id) REFERENCES reservation(reservation_id)
);