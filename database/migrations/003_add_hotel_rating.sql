ALTER TABLE hotels
ADD COLUMN stars INTEGER DEFAULT 3;


ALTER TABLE hotels
ADD COLUMN description TEXT;


ALTER TABLE hotels
ADD COLUMN amenities TEXT[];


ALTER TABLE hotels
ADD CONSTRAINT chk_hotel_stars
CHECK (
    stars >= 1
    AND stars <= 5
);