# from cx_Oracle import*
# # cafe 상품 조회
# def cafe_select():
#     conn=connect('hr/hr@localhost:1521/xe')
#     cur=conn.cursor()
#     cur.execute('select*from cafe order by code')
#     # 튜플 조회
#     # for x in cur:
#     #     print(x)
#     # 언패킹 조회
#     for code,itemname,type1,price,bigo in cur:
#         print(code,itemname,type1,price,bigo)
#     cur.close()
#     conn.commit()
#     conn.close()
# # cafe_select()
#
# # 상품 등록
# def cafe_insert(data):
#     conn=connect('hr/hr@localhost:1521/xe')
#     cur=conn.cursor()
#     cur.execute('insert into cafe(code,itemname,type1,price,bigo) values(:1,:2,:3,:4,:5)',data)
#     cur.close()
#     conn.commit()
#     conn.close()
# # cafe_insert()
#
# #상품 삭제
# def cafe_delete(data):
#     conn=connect('hr/hr@localhost:1521/xe')
#     cur=conn.cursor()
#     cur.execute('delete from cafe where code=:1',data)
#     cur.close()
#     conn.commit()
#     conn.close()
# # cafe_delete()
#
# # 상품 변경
# def cafe_update(data):
#     conn=connect('hr/hr@localhost:1521/xe')
#     cur=conn.cursor()
#     cur.execute('update cafe set itemname = :1 where code = :2',data)
#     cur.close()
#     conn.commit()
#     conn.close()


