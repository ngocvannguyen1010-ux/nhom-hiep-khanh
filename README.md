# Nhôm Hiệp Khanh

Web demo bán đồ nhôm gia dụng (chậu, mâm, xoong nồi) — bài tập fullstack.

**Stack:** Next.js (frontend) + FastAPI (backend) + PostgreSQL + Railway.

## Cấu trúc

```
nhom-hiep-khanh/
├── backend/           # FastAPI + SQLAlchemy
├── frontend/          # Next.js (App Router) + Tailwind  [đang phát triển]
├── docker-compose.yml # Postgres local
└── README.md
```

## Chạy local — backend

Yêu cầu: Docker Desktop, Python 3.10+.

```bash
# 1. Khởi động Postgres
docker compose up -d

# 2. Cài dependencies
cd backend
python -m venv .venv
.venv\Scripts\activate         # Windows
# source .venv/bin/activate    # Linux/Mac
pip install -r requirements.txt

# 3. Copy env và seed dữ liệu
copy .env.example .env
python seed.py

# 4. Chạy server
uvicorn app.main:app --reload
```

Mở `http://localhost:8000/docs` xem Swagger UI.

## API endpoints

- `GET /categories` — danh sách danh mục
- `GET /products?category=<slug>&featured=<bool>` — danh sách sản phẩm
- `GET /products/{slug}` — chi tiết sản phẩm
- `POST /orders` — tạo đơn hàng
- `GET /orders/{id}` — xem đơn hàng

## Deploy backend trên Railway

1. Tạo project mới trên [railway.app](https://railway.app), kết nối GitHub repo này
2. Thêm service **PostgreSQL** (Add Service → Database → Postgres)
3. Thêm service từ GitHub repo, set **Root Directory** = `backend`
4. Set biến môi trường cho service backend:
   - `DATABASE_URL` = `${{Postgres.DATABASE_URL}}` (reference từ Postgres service)
   - `CORS_ORIGINS` = URL frontend (sau khi deploy frontend, thêm vào)
5. Service tự build từ `backend/Dockerfile` và start theo `backend/railway.json`
6. Vào tab Settings → Networking → **Generate Domain** để có URL public

Backend tự động seed data khi khởi động lần đầu (xem `startCommand` trong `railway.json`).

## Frontend

Đang phát triển. Sẽ cập nhật commit kế tiếp.
