# Week 3 notes

## Part B: curl status codes
1. POST /notes (valid): 201
2. GET /notes/1: 200
3. GET /notes/999: 404
4. PATCH /notes/1: 200
5. POST /notes with "owner": 422
6. GET /notes?limit=1000: 422
7. DELETE /notes/1: 204
