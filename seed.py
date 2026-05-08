"""Seed san pham mau cho Nhom Hiep Khanh.

Chay:
    python seed.py
"""
from app.database import Base, SessionLocal, engine
from app.models import Category, Product, Order, OrderItem


def reset_data(db):
    db.query(OrderItem).delete()
    db.query(Order).delete()
    db.query(Product).delete()
    db.query(Category).delete()
    db.commit()


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        reset_data(db)

        cat_chau = Category(
            slug="chau-nhom",
            name="Chậu nhôm",
            description="Chậu nhôm đúc nguyên khối, dày dặn, dùng được nhiều năm.",
        )
        cat_mam = Category(
            slug="mam-nhom",
            name="Mâm nhôm",
            description="Mâm nhôm truyền thống, đa dạng kích thước cho gia đình và quán ăn.",
        )
        cat_xoong = Category(
            slug="xoong-noi-nhom",
            name="Xoong nồi nhôm",
            description="Xoong nồi nhôm dẫn nhiệt nhanh, tiết kiệm gas, phù hợp bếp Việt.",
        )
        db.add_all([cat_chau, cat_mam, cat_xoong])
        db.flush()

        img_chau = "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=800"
        img_mam = "https://images.unsplash.com/photo-1584990347449-a8d2d6cd0e10?w=800"
        img_xoong = "https://images.unsplash.com/photo-1584990347163-7ab5e7c4d4d3?w=800"

        products = [
            Product(
                slug="chau-nhom-duc-40cm",
                name="Chậu nhôm đúc 40cm",
                description="Chậu đúc nguyên khối, đường kính 40cm, dày 3mm.",
                long_description=(
                    "Chậu nhôm đúc 40cm là sản phẩm chủ lực của xưởng Nhôm Hiệp Khanh, "
                    "đúc nguyên khối từ nhôm tinh luyện. Thành chậu dày 3mm, "
                    "đáy phẳng đặt vững trên mọi bề mặt. Phù hợp rửa rau, vo gạo, "
                    "ngâm đồ cho gia đình 4-6 người."
                ),
                price=185000,
                original_price=210000,
                images=[img_chau],
                specs={"Đường kính": "40cm", "Độ dày": "3mm", "Trọng lượng": "1.2kg"},
                featured=True,
                category_id=cat_chau.id,
            ),
            Product(
                slug="chau-nhom-duc-50cm",
                name="Chậu nhôm đúc 50cm",
                description="Chậu cỡ lớn cho quán ăn, gia đình đông người.",
                long_description=(
                    "Phiên bản 50cm dành cho quán ăn, nhà hàng. Chứa được 15-20 lít nước, "
                    "rửa lượng lớn rau củ trong một lần. Vành chậu cuốn dày, không sắc tay."
                ),
                price=265000,
                images=[img_chau],
                specs={"Đường kính": "50cm", "Độ dày": "3.5mm", "Trọng lượng": "1.8kg"},
                category_id=cat_chau.id,
            ),
            Product(
                slug="chau-nhom-mong-30cm",
                name="Chậu nhôm mỏng 30cm",
                description="Chậu nhỏ gọn, nhẹ, dùng hàng ngày.",
                price=85000,
                images=[img_chau],
                specs={"Đường kính": "30cm", "Độ dày": "1.5mm"},
                category_id=cat_chau.id,
            ),
            Product(
                slug="chau-nhom-co-tay-cam",
                name="Chậu nhôm có tay cầm",
                description="Chậu 35cm, tay cầm chắc chắn, tiện bưng bê.",
                price=145000,
                images=[img_chau],
                specs={"Đường kính": "35cm", "Tay cầm": "Có"},
                category_id=cat_chau.id,
            ),
            Product(
                slug="mam-nhom-tron-50cm",
                name="Mâm nhôm tròn 50cm",
                description="Mâm tròn truyền thống, đường kính 50cm.",
                long_description=(
                    "Mâm nhôm tròn được dập thủ công tại làng nghề, vành mâm cuốn dày "
                    "không sắc tay. Bề mặt nhẵn bóng, dễ vệ sinh. Dùng được cho mâm cỗ, "
                    "đám giỗ, hội họp gia đình."
                ),
                price=175000,
                original_price=200000,
                images=[img_mam],
                specs={"Đường kính": "50cm", "Hình dáng": "Tròn"},
                featured=True,
                category_id=cat_mam.id,
            ),
            Product(
                slug="mam-nhom-tron-60cm",
                name="Mâm nhôm tròn 60cm",
                description="Mâm cỡ lớn cho cỗ 8-10 người.",
                price=235000,
                images=[img_mam],
                specs={"Đường kính": "60cm", "Hình dáng": "Tròn"},
                category_id=cat_mam.id,
            ),
            Product(
                slug="mam-nhom-chu-nhat",
                name="Mâm nhôm chữ nhật 40x50cm",
                description="Mâm chữ nhật, phù hợp bưng bê khay đồ ăn.",
                price=195000,
                images=[img_mam],
                specs={"Kích thước": "40x50cm", "Hình dáng": "Chữ nhật"},
                category_id=cat_mam.id,
            ),
            Product(
                slug="mam-nhom-vuong-45cm",
                name="Mâm nhôm vuông 45cm",
                description="Mâm vuông, gọn gàng, hiện đại.",
                price=185000,
                images=[img_mam],
                specs={"Kích thước": "45x45cm", "Hình dáng": "Vuông"},
                category_id=cat_mam.id,
            ),
            Product(
                slug="xoong-nhom-22cm",
                name="Xoong nhôm 22cm",
                description="Xoong nhôm 2 tay quai, đáy dày, dẫn nhiệt nhanh.",
                long_description=(
                    "Xoong nhôm 22cm phù hợp nấu canh, kho cá cho gia đình 4 người. "
                    "Đáy xoong dày 4mm hạn chế cháy khét, tiết kiệm gas. Hai quai cứng cáp, "
                    "không nóng tay khi nấu."
                ),
                price=155000,
                images=[img_xoong],
                specs={"Đường kính": "22cm", "Dung tích": "3 lít", "Đáy": "Dày 4mm"},
                featured=True,
                category_id=cat_xoong.id,
            ),
            Product(
                slug="xoong-nhom-26cm",
                name="Xoong nhôm 26cm",
                description="Xoong cỡ vừa, dung tích 5 lít.",
                price=195000,
                images=[img_xoong],
                specs={"Đường kính": "26cm", "Dung tích": "5 lít"},
                category_id=cat_xoong.id,
            ),
            Product(
                slug="xoong-nhom-30cm",
                name="Xoong nhôm 30cm",
                description="Xoong lớn cho quán phở, quán bún.",
                price=265000,
                images=[img_xoong],
                specs={"Đường kính": "30cm", "Dung tích": "8 lít"},
                category_id=cat_xoong.id,
            ),
            Product(
                slug="noi-nhom-co-nap-24cm",
                name="Nồi nhôm có nắp 24cm",
                description="Nồi nhôm kèm nắp đậy kín, dung tích 4 lít.",
                price=215000,
                original_price=245000,
                images=[img_xoong],
                specs={"Đường kính": "24cm", "Dung tích": "4 lít", "Nắp": "Có"},
                featured=True,
                category_id=cat_xoong.id,
            ),
            Product(
                slug="noi-nhom-hap-28cm",
                name="Nồi nhôm hấp 28cm",
                description="Nồi hấp 2 tầng, hấp xôi/bánh dễ dàng.",
                price=345000,
                images=[img_xoong],
                specs={"Đường kính": "28cm", "Số tầng": "2"},
                category_id=cat_xoong.id,
            ),
        ]
        db.add_all(products)
        db.commit()
        print(f"Da seed {len(products)} san pham trong 3 danh muc.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
