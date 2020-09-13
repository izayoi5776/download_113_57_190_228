CREATE TABLE if not exists pos (
              STCD text PRIMARY KEY,
              RVNM text,
              STNM text,
              FRZ text,
              GRZ text,
              WRZ text,
              MAXZ text);
insert into pos values('60105400','长江','寸滩','','','','') ON CONFLICT DO NOTHING;
insert into pos values('60803000','长江','武隆','','','','') ON CONFLICT DO NOTHING;
insert into pos values('60107300','长江','宜昌','52.00','55.73','53.00','55.92') ON CONFLICT DO NOTHING;
insert into pos values('60107400','长江','枝城','48.00','51.75','49.00','50.75') ON CONFLICT DO NOTHING;
insert into pos values('60108300','长江','沙市','42.00','45.00','43.00','45.22') ON CONFLICT DO NOTHING;
insert into pos values('60110500','长江','监利','34.50','37.23','35.50','') ON CONFLICT DO NOTHING;
insert into pos values('60111200','长江','莲花塘','','34.40','32.50','35.80') ON CONFLICT DO NOTHING;
insert into pos values('60111300','长江','螺山','31.00','','34.95','32.00') ON CONFLICT DO NOTHING;
insert into pos values('60112200','长江','汉口','25.00','29.73','29.73','27.30') ON CONFLICT DO NOTHING;
insert into pos values('60112900','长江','黄石','22.80','27.50','24.50','26.39') ON CONFLICT DO NOTHING;
insert into pos values('60113205','长江','码头镇','20.50','24.50','21.50','24.04') ON CONFLICT DO NOTHING;
insert into pos values('60113400','长江','九江','19.50','23.25','20.00','23.03') ON CONFLICT DO NOTHING;
insert into pos values('60106980','长江','三峡水库','','','','') ON CONFLICT DO NOTHING;
insert into pos values('61512000','洞庭湖','城陵矶','','34.55','32.50','35.94') ON CONFLICT DO NOTHING;
insert into pos values('62601600','鄱阳湖','湖口','','22.50','19.50','22.59') ON CONFLICT DO NOTHING;
insert into pos values('61102000','湘江','湘潭','','39.50','38.00','41.95') ON CONFLICT DO NOTHING;
insert into pos values('61202100','资水','桃江','','42.30','39.20','44.44') ON CONFLICT DO NOTHING;
insert into pos values('61302800','沅水','桃源','','45.40','42.50','47.37') ON CONFLICT DO NOTHING;
insert into pos values('61400900','澧水','石门','','61.00','58.50','62.66') ON CONFLICT DO NOTHING;
insert into pos values('61500300','松滋河','新江口','43.00','45.77','44.00','46.18') ON CONFLICT DO NOTHING;
insert into pos values('61501200','松滋河','沙道观','43.00','','44.00','') ON CONFLICT DO NOTHING;
insert into pos values('61502200','藕池河','管家铺','37.50','39.50','38.50','40.28') ON CONFLICT DO NOTHING;
insert into pos values('61501800','藕池河','康家岗','37.50','39.87','38.50','40.44') ON CONFLICT DO NOTHING;
insert into pos values('61501500','虎渡河','弥陀寺','42.00','44.15','43.00','44.90') ON CONFLICT DO NOTHING;
insert into pos values('61014500','长湖','长湖','31.50','33.00','32.50','33.46') ON CONFLICT DO NOTHING;
insert into pos values('61018000','洪湖','挖沟咀','25.80','26.97','26.20','27.19') ON CONFLICT DO NOTHING;
insert into pos values('62210820','刁汊湖','余家咀','25.00','26.87','25.70','') ON CONFLICT DO NOTHING;
insert into pos values('61714000','斧头湖','三洲','21.50','23.94','22.80','24.59') ON CONFLICT DO NOTHING;
insert into pos values('61602600','梁子湖','梁子镇','19.00','21.36','20.50','21.49') ON CONFLICT DO NOTHING;
insert into pos values('61801300','汉江','安康','','','','259.26') ON CONFLICT DO NOTHING;
insert into pos values('61801700','汉江','白河','','191.00','187.00','196.63') ON CONFLICT DO NOTHING;
insert into pos values('61802800','汉江','黄家港','','','','96.45') ON CONFLICT DO NOTHING;
insert into pos values('61803400','汉江','襄阳','65.50','70.00','67.00','71.71') ON CONFLICT DO NOTHING;
insert into pos values('61803500','汉江','宜城','56.50','59.30','57.50','61.45') ON CONFLICT DO NOTHING;
insert into pos values('61804110','汉江','皇庄','47.00','50.62','48.00','52.30') ON CONFLICT DO NOTHING;
insert into pos values('61804210','汉江','沙洋','40.80','44.50','41.80','44.50') ON CONFLICT DO NOTHING;
insert into pos values('61804400','汉江','岳口','36.90','40.62','37.90','40.62') ON CONFLICT DO NOTHING;
insert into pos values('61804600','汉江','仙桃','34.10','36.20','35.10','36.24') ON CONFLICT DO NOTHING;
insert into pos values('61804710','汉江','汉川','28.00','31.69','29.00','32.09') ON CONFLICT DO NOTHING;
insert into pos values('61802700','汉江','丹江口水库','','','','') ON CONFLICT DO NOTHING;
insert into pos values('61002791','清江','水布垭','','','','') ON CONFLICT DO NOTHING;
insert into pos values('61003101','清江','隔河岩','','','','') ON CONFLICT DO NOTHING;
insert into pos values('60908000','沮漳河','河溶','47.50','50.00','48.50','50.49') ON CONFLICT DO NOTHING;
insert into pos values('62213000','东荆河','潜江','38.40','42.11','39.70','42.09') ON CONFLICT DO NOTHING;
insert into pos values('62206900','汉北河','天门','28.30','30.00','29.30','31.35') ON CONFLICT DO NOTHING;
insert into pos values('62209400','大富水','应城','27.50','33.00','29.00','33.01') ON CONFLICT DO NOTHING;
insert into pos values('62205600','环水','花园','','39.95','37.50','39.95') ON CONFLICT DO NOTHING;
insert into pos values('62205800','环水','孝感','26.50','31.00','27.50','32.28') ON CONFLICT DO NOTHING;
insert into pos values('62201400','府河','隔蒲潭','29.50','33.50','30.50','33.57') ON CONFLICT DO NOTHING;
insert into pos values('62201800','府澴河','卧龙潭','26.50','29.69','27.00','31.19') ON CONFLICT DO NOTHING;
insert into pos values('61607000','富水','阳新','20.00','22.50','21.50','23.69') ON CONFLICT DO NOTHING;
insert into pos values('61609400','滠水','黄陂','25.00','29.31','26.00','29.31') ON CONFLICT DO NOTHING;
insert into pos values('61610600','倒水','李家集','26.30','30.73','28.00','30.76') ON CONFLICT DO NOTHING;
insert into pos values('61612400','举水','柳子港','28.00','33.11','29.00','33.58') ON CONFLICT DO NOTHING;
insert into pos values('61615600','巴水','马家潭','','','','') ON CONFLICT DO NOTHING;
insert into pos values('61619600','蕲水','西河驿','','','','') ON CONFLICT DO NOTHING;
