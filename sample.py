# # import pandas as pd
# # #
# # # res = []
# # # df = pd.read_json("C:\\Users\\e5567006\\Documents\\workspace\\ruf-api\\util\\15.json")
# # # columns = list(df.columns.values)
# # # col_dtypes = list(df.dtypes.values)
# # # for index, col in enumerate(columns):
# # #     dObj = {}
# # #     dObj['field'] = col
# # #     dObj['enableRowGroup'] = True
# # #     dObj['sortable'] = True
# # #     res.append(dObj)
# # # return res
# #
# # # def get_cat_recon(user_id, rpt_id, fe_id, filterData, prod_line, user_spec, fe_int_id, prod_grp):
# # #     output = {}
# # #     detail_col_lst = []
# # #     res = {}
# # #     list_of_files = glob.glob(DIR + rpt_id + '*.csv') # * means all if need specific format then *.csv
# # #     f_name = max(list_of_files, key=os.path.getctime)
# # #     df_rec = pd.read_csv(f_name)
# # #     locale = user_spec['locale'].replace("-", "_")
# # #     def format_curr(x):
# # #         try:
# # #             return format_currency(x, '', locale=locale)
# # #         except Exception as e:
# # #             return ""
# # #     for column in list(df_rec.select_dtypes(['float64']).columns):
# # #         df_rec[column] = df_rec[column].apply(lambda x :format_curr(x))
# # #     data_head = list(df_rec.columns.values)
# # #     format_type = str(get_format_type(rpt_id, fe_id, fe_int_id))
# # #     rpt_col = get_cat1_headers(rpt_id, fe_id, fe_int_id)
# # #     if len(rpt_col) < 0:
# # #         raise Exception(constants.RptHeaderErr, "Headers len(0)")
# # #     alignment = {}
# # #     data_typ = {}
# # #     pdf_conf = {}
# # #     data_len = {}
# # #     for col in rpt_col:
# # #         alignment[col.clmn_nme] = col.alignment
# # #         data_typ[col.clmn_nme] = col.data_typ
# # #         data_len[col.clmn_nme] = col.data_len
# # #     col_def = handler.HeadersUtil().convert_headers(rpt_col)
# # #     for cl in col_def:
# # #         detail_col_lst.append(cl['field'])
# # #         cl['enableRowGroup'] = True
# # #         if cl['data_type'].lower() == 'numeric':
# # #             cl['enableValue'] = True
# # #     pdf_conf['alignMent'] = alignment
# # #     pdf_conf['data_type'] = data_typ
# # #     pdf_conf['data_length'] = data_len
# # #     output['pdf_conf'] = pdf_conf
# # #     output['columnDef'] = col_def
# # #     output['columnValue'] = json.loads(df_rec.to_json(orient='records'))
# # #     res['detail'] = output
# # #     rpt_maint = get_rpt_by_id(rpt_id, fe_id, fe_int_id)
# # #     #try:
# # #         #if 0 < len(rpt_maint) < 2:
# # #             #res['report_note'] = rpt_maint[0].rpt_notes
# # #     #except Exception as e:
# # #         #raise Exception(constants.RptMaintErr, e)
# # #     res['cat'] = format_type.lower()
# # #     return res
# #
# # # import pandas as pd
# # # import tabula
# # # import pdfkit
# # # file_path = "C:\\Users\\e5567006\\Desktop\\ac027114.pdf"
# # #
# # # #"https://github.com/chezou/tabula-py/raw/master/tests/resources/data.pdf"#
# # #
# # # # df = tabula.read_pdf(file_path, encoding='utf-8', pages='3')
# # # # d = pdfkit.
# # # # import PyPDF2
# # # # # file = open(file_path, 'rb')
# # # # # file_r = PyPDF2.PdfFileReader(file)
# # # # #
# # # import textract
# # #
# # # d = textract.process("C:\\Users\\e5567006\\Desktop\\ac027114.pdf")
# #
# # # import itertools
# # # import threading
# # # import time
# # # import sys
# # #
# # # done = False
# # # #here is the animation
# # # def animate():
# # #     for c in itertools.cycle(['|', '/', '-', '\\']):
# # #         if done:
# # #             break
# # #         sys.stdout.write('\rloading ' + c)
# # #         sys.stdout.flush()
# # #         time.sleep(0.1)
# # #     sys.stdout.write('\rDone!     ')
# # #
# # # t = threading.Thread(target=animate)
# # # t.start()
# # #
# # # #long process here
# # # time.sleep(10)
# # # done = True
# #
# # import ply.lex as lex, re
# #
# # tokens = (
# #     "TABLE",
# #     "JOIN",
# #     "COLUMN",
# #     "TRASH"
# # )
# #
# # tables = {"tables": {}, "alias": {}}
# # columns = []
# #
# # t_TRASH = r"Select|on|=|;|\s+|,|\t|\r"
# #
# # def t_TABLE(t):
# #     r"from\s(\w+)\sas\s(\w+)"
# #
# #     regex = re.compile(t_TABLE.__doc__)
# #     m = regex.search(t.value)
# #     if m is not None:
# #         tbl = m.group(1)
# #         alias = m.group(2)
# #         tables["tables"][tbl] = ""
# #         tables["alias"][alias] = tbl
# #
# #     return t
# #
# # def t_JOIN(t):
# #     r"inner\s+join\s+(\w+)\s+as\s+(\w+)"
# #
# #     regex = re.compile(t_JOIN.__doc__)
# #     m = regex.search(t.value)
# #     if m is not None:
# #         tbl = m.group(1)
# #         alias = m.group(2)
# #         tables["tables"][tbl] = ""
# #         tables["alias"][alias] = tbl
# #     return t
# #
# # def t_COLUMN(t):
# #     r"(\w+\.\w+)"
# #
# #     regex = re.compile(t_COLUMN.__doc__)
# #     m = regex.search(t.value)
# #     if m is not None:
# #         t.value = m.group(1)
# #         columns.append(t.value)
# #     return t
# #
# # def t_error(t):
# #     raise TypeError("Unknown text '%s'" % (t.value,))
# #     t.lexer.skip(len(t.value))
# #
# # # here is where the magic starts
# # # def mylex(inp):
# # #     lexer = lex.lex()
# # #     lexer.input(inp)
# # #
# # #     for token in lexer:
# # #         pass
# # #
# # #     result = {}
# # #     for col in columns:
# # #         tbl, c = col.split('.')
# # #         if tbl in tables["alias"].keys():
# # #             key = tables["alias"][tbl]
# # #         else:
# # #             key = tbl
# # #
# # #         if key in result:
# # #             result[key].append(c)
# # #         else:
# # #             result[key] = list()
# # #             result[key].append(c)
# # #
# # #     print(result)
# # #     # {'tb1': ['col1', 'col7'], 'tb2': ['col2', 'col8']}
# # #
# # # string = "Select a.col1, b.col2 from tb1 as a inner join tb2 as b on tb1.col7 = tb2.col8;"
# # # mylex(string)
# import re
#
#
# st = "sdfsdfsdf10fdsfsdfd1111vdsfsdf0000fsdfsd11"
# st.isdigit()
# print(''.join([l for l in list(st) if l.isdigit()]))
#
# # re.findall()
# print("".join(sorted((''.join(i for i in "sdfsdfsdf10fdsfsdfd1111vdsfsdf0000fsdfsd11" if i.isdigit())), reverse=True)))


data = {
              "columnDef": [{
                                           "field": "rtd_crrnt_mtrty_amt",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_rtd_crrnt_mtrty_amt",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Cur Mat Amt",
                                           "data_type": "decimal",
                                           "allowedAggFuncs": [
                                                          "avg",
                                                          "count",
                                                          "sum",
                                                          "max",
                                                          "min"
                                           ],
                                           "enableRowGroup": True,
                                           "sortable": True,
                                           "isNum": True
                             },
                             {
                                           "field": "full_date_txt",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_full_date_txt",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Booking Date",
                                           "data_type": "date",
                                           "enableRowGroup": True,
                                           "sortable": True
                             },
                             {
                                           "field": "ar_id_item",
                                           "DataID": "rt_ar_dly_bal_dp_rd_ar_id_item",
                                           "tbl_name": "rt_ar_dly_bal_dp_rd",
                                           "headerName": "Acct #",
                                           "data_type": "string",
                                           "enableRowGroup": True,
                                           "sortable": True
                             },
                             {
                                           "field": "ldgr_bal",
                                           "DataID": "rt_ar_dly_bal_dp_rd_ldgr_bal",
                                           "tbl_name": "rt_ar_dly_bal_dp_rd",
                                           "headerName": "Ledger Bal",
                                           "data_type": "decimal",
                                           "enableRowGroup": True,
                                           "sortable": True,
                                           "isNum": True
                             },
                             {
                                           "field": "avail_bal",
                                           "DataID": "rt_ar_dly_bal_dp_rd_avail_bal",
                                           "tbl_name": "rt_ar_dly_bal_dp_rd",
                                           "headerName": "Available Bal",
                                           "data_type": "decimal",
                                           "enableRowGroup": True,
                                           "sortable": True,
                                           "isNum": True,
                                           "operator": "="
                             },
                             {
                                           "field": "rtd_grace_end_date",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_rtd_grace_end_date",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Grace End Date",
                                           "data_type": "date",
                                           "enableRowGroup": True,
                                           "sortable": True
                             },
                             {
                                           "field": "csi_code",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_csi_code",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Instruction Code",
                                           "data_type": "string",
                                           "enableRowGroup": True,
                                           "sortable": True
                             },
                             {
                                           "field": "abdcs_auf_lmt_exp_date",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_abdcs_auf_lmt_exp_date",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Expiry Date",
                                           "data_type": "date",
                                           "enableRowGroup": True,
                                           "sortable": True
                             },
                             {
                                           "field": "apacs_fund_owner",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_apacs_fund_owner",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Fund Owner",
                                           "data_type": "string",
                                           "enableRowGroup": True,
                                           "sortable": True
                             },
                             {
                                           "field": "apd_name",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_apd_name",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Product Name",
                                           "data_type": "string",
                                           "enableRowGroup": True,
                                           "sortable": True
                             },
                             {
                                           "field": "apd_code",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_apd_code",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Product Code",
                                           "data_type": "string",
                                           "enableRowGroup": True,
                                           "sortable": True,
                                           "operator": "="
                             },
                             {
                                           "field": "enart_value",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_enart_value",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Ent Acct Type",
                                           "data_type": "string",
                                           "enableRowGroup": True,
                                           "sortable": True
                             },
                             {
                                           "field": "frst_dpst_efctv_date",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_frst_dpst_efctv_date",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Effective Date",
                                           "data_type": "date",
                                           "enableRowGroup": True,
                                           "sortable": True
                             }
              ],
              "filters": {
                             "condition": "and",
                             "rules": [{
                                                          "field": "avail_bal",
                                                          "operator": "=",
                                                          "entity": "IGNxxx",
                                                          "tableID": "",
                                                          "data_type": "decimal",
                                                          "DataID": "rt_ar_dly_bal_dp_rd_avail_bal",
                                                          "value": "60"
                                           },
                                           {
                                                          "field": "apd_code",
                                                          "operator": "=",
                                                          "entity": "IGNxxx",
                                                          "tableID": "",
                                                          "data_type": "string",
                                                          "DataID": "rt_apd_ar_mstr_dp_rd_apd_code",
                                                          "value": "MMDA"
                                           }
                             ]
              },
              "isTable": False,
              "is_ui_based": False,
              "newRptID": "IGNxxx",
              "prod_line": "RD",
              "query": "select RT_APD_AR_MSTR_DP_RD.RTD_CRRNT_MTRTY_AMT,RT_APD_AR_MSTR_DP_RD.FULL_DATE_TXT,RT_AR_DLY_BAL_DP_RD.AR_ID_ITEM,RT_AR_DLY_BAL_DP_RD.LDGR_BAL,RT_AR_DLY_BAL_DP_RD.AVAIL_BAL,RT_APD_AR_MSTR_DP_RD.RTD_GRACE_END_DATE,RT_APD_AR_MSTR_DP_RD.CSI_CODE,RT_APD_AR_MSTR_DP_RD.ABDCS_AUF_LMT_EXP_DATE,RT_APD_AR_MSTR_DP_RD.APACS_FUND_OWNER,RT_APD_AR_MSTR_DP_RD.APD_NAME,RT_APD_AR_MSTR_DP_RD.APD_CODE,RT_APD_AR_MSTR_DP_RD.ENART_VALUE,RT_APD_AR_MSTR_DP_RD.FRST_DPST_EFCTV_DATE from RT_APD_AR_MSTR_DP_RD left join RT_AR_DLY_BAL_DP_RD on RT_APD_AR_MSTR_DP_RD.ar_id_item=RT_AR_DLY_BAL_DP_RD.ar_id_item and RT_APD_AR_MSTR_DP_RD.ldbid=RT_AR_DLY_BAL_DP_RD.ldbid",
              "conn_method": "hive",
              "params": {
                             "startRow": 0,
                             "endRow": 99,
                             "rowGroupCols": [{
                                           "id": "ar_id_item",
                                           "displayName": "Acct #",
                                           "field": "ar_id_item"
                             }],
                             "valueCols": [{
                                           "id": "avail_bal",
                                           "aggFunc": "sum",
                                           "displayName": "Available Bal",
                                           "field": "avail_bal"
                             }],
                             "pivotCols": [],
                             "pivotMode": False,
                             "groupKeys": [],
                             "filterModel": {},
                             "sortModel": []
              },
              "cacheCode": "c21a076e-2a82-4619-8f20-7a0d992fa82f",
              "editFlag": False,
              "columns": [{
                                           "tab": "detail",
                                           "tab_title": "Details",
                                           "data": [{
                                                                        "column_name": "rtd_crrnt_mtrty_amt",
                                                                        "seq_order": 1,
                                                                        "data_type": "decimal",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_rtd_crrnt_mtrty_amt",
                                                                        "alignment": "Right",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "full_date_txt",
                                                                        "seq_order": 2,
                                                                        "data_type": "date",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_full_date_txt",
                                                                        "alignment": "Center",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "ar_id_item",
                                                                        "seq_order": 3,
                                                                        "data_type": "string",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_ar_dly_bal_dp_rd_ar_id_item",
                                                                        "alignment": "Left",
                                                                        "tbl_name": "rt_ar_dly_bal_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "ldgr_bal",
                                                                        "seq_order": 4,
                                                                        "data_type": "decimal",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_ar_dly_bal_dp_rd_ldgr_bal",
                                                                        "alignment": "Right",
                                                                        "tbl_name": "rt_ar_dly_bal_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "avail_bal",
                                                                        "seq_order": 5,
                                                                        "data_type": "decimal",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_ar_dly_bal_dp_rd_avail_bal",
                                                                        "alignment": "Right",
                                                                        "tbl_name": "rt_ar_dly_bal_dp_rd",
                                                                        "validValueConfig": {
                                                                                      "column_name": "Available Bal",
                                                                                      "DataID": "rt_ar_dly_bal_dp_rd_avail_bal",
                                                                                      "rpt_sp_param_name": "P_avail_bal",
                                                                                      "sequence_order": 1,
                                                                                      "filter_type": "text",
                                                                                      "fltr_oprtr": "=",
                                                                                      "field": "avail_bal"
                                                                        }
                                                          },
                                                          {
                                                                        "column_name": "rtd_grace_end_date",
                                                                        "seq_order": 6,
                                                                        "data_type": "date",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_rtd_grace_end_date",
                                                                        "alignment": "Center",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "csi_code",
                                                                        "seq_order": 7,
                                                                        "data_type": "string",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_csi_code",
                                                                        "alignment": "Left",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "abdcs_auf_lmt_exp_date",
                                                                        "seq_order": 8,
                                                                        "data_type": "date",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_abdcs_auf_lmt_exp_date",
                                                                        "alignment": "Center",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "apacs_fund_owner",
                                                                        "seq_order": 9,
                                                                        "data_type": "string",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_apacs_fund_owner",
                                                                        "alignment": "Left",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "apd_name",
                                                                        "seq_order": 10,
                                                                        "data_type": "string",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_apd_name",
                                                                        "alignment": "Left",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "apd_code",
                                                                        "seq_order": 11,
                                                                        "data_type": "string",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_apd_code",
                                                                        "alignment": "Left",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {
                                                                                      "column_name": "Product Code",
                                                                                      "DataID": "rt_apd_ar_mstr_dp_rd_apd_code",
                                                                                      "rpt_sp_param_name": "P_apd_code",
                                                                                      "sequence_order": 2,
                                                                                      "filter_type": "text",
                                                                                      "fltr_oprtr": "=",
                                                                                      "field": "apd_code"
                                                                        }
                                                          },
                                                          {
                                                                        "column_name": "enart_value",
                                                                        "seq_order": 12,
                                                                        "data_type": "string",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_enart_value",
                                                                        "alignment": "Left",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "frst_dpst_efctv_date",
                                                                        "seq_order": 13,
                                                                        "data_type": "date",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_frst_dpst_efctv_date",
                                                                        "alignment": "Center",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {}
                                                          }
                                           ]
                             },
                             {
                                           "tab": "summary",
                                           "tab_title": "Sum of Ledger Bal",
                                           "data": [{
                                                                        "column_name": "ar_id_item",
                                                                        "seq_order": 1,
                                                                        "data_type": "string",
                                                                        "isGrp": True,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_ar_dly_bal_dp_rd_ar_id_item",
                                                                        "alignment": "Left",
                                                                        "tbl_name": "rt_ar_dly_bal_dp_rd",
                                                                        "is_grp": "Y",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "ldgr_bal",
                                                                        "seq_order": 2,
                                                                        "data_type": "decimal",
                                                                        "isGrp": False,
                                                                        "aggFunc": "sum",
                                                                        "column_width": "200",
                                                                        "DataID": "rt_ar_dly_bal_dp_rd_ldgr_bal",
                                                                        "alignment": "Right",
                                                                        "tbl_name": "rt_ar_dly_bal_dp_rd",
                                                                        "is_grp": "N",
                                                                        "validValueConfig": {}
                                                          }
                                           ]
                             },
                             {
                                           "tab": "summary",
                                           "tab_title": "Sum of Available Bal",
                                           "data": [{
                                                                        "column_name": "ar_id_item",
                                                                        "seq_order": 1,
                                                                        "data_type": "string",
                                                                        "isGrp": True,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_ar_dly_bal_dp_rd_ar_id_item",
                                                                        "alignment": "Left",
                                                                        "tbl_name": "rt_ar_dly_bal_dp_rd",
                                                                        "is_grp": "Y",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "avail_bal",
                                                                        "seq_order": 2,
                                                                        "data_type": "decimal",
                                                                        "isGrp": False,
                                                                        "aggFunc": "sum",
                                                                        "column_width": "200",
                                                                        "DataID": "rt_ar_dly_bal_dp_rd_avail_bal",
                                                                        "alignment": "Right",
                                                                        "tbl_name": "rt_ar_dly_bal_dp_rd",
                                                                        "is_grp": "N",
                                                                        "validValueConfig": {
                                                                                      "column_name": "Available Bal",
                                                                                      "DataID": "rt_ar_dly_bal_dp_rd_avail_bal",
                                                                                      "rpt_sp_param_name": "P_avail_bal",
                                                                                      "sequence_order": 1,
                                                                                      "filter_type": "text",
                                                                                      "fltr_oprtr": "=",
                                                                                      "field": "avail_bal"
                                                                        }
                                                          }
                                           ]
                             }
              ],
              "max_sum_cols": 2,
              "sav_rpt": {
                             "name": "Multitab_join_11",
                             "cat": "TXN",
                             "desc": "A query based multitab join with aggregations",
                             "downloadType": "PDF,EXCEL,TXT",
                             "configuration": "Header,Footer",
                             "connectivity": "hive",
                             "reportFormat": "MultiTab"
              }
}


# data['columns']['data']

# temp_lst = [j['data'] for j in [i for i in data['columns'] if i['tab'] != "detail"]]

# print(temp_lst)

# for i in range(lentemp_lst:
#     for j in temp_lst

# for i in range(len(temp_lst) - 1):
#     for data in range(len(sum.data) - 1):
#         pass

# js = [
#     {
#                                                                         "column_name": "rtd_crrnt_mtrty_amt",
#                                                                         "seq_order": 1,
#                                                                         "data_type": "decimal",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_rtd_crrnt_mtrty_amt",
#                                                                         "alignment": "Right",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "full_date_txt",
#                                                                         "seq_order": 2,
#                                                                         "data_type": "date",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_full_date_txt",
#                                                                         "alignment": "Center",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "ar_id_item",
#                                                                         "seq_order": 3,
#                                                                         "data_type": "string",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_ar_dly_bal_dp_rd_ar_id_item",
#                                                                         "alignment": "Left",
#                                                                         "tbl_name": "rt_ar_dly_bal_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "ldgr_bal",
#                                                                         "seq_order": 4,
#                                                                         "data_type": "decimal",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_ar_dly_bal_dp_rd_ldgr_bal",
#                                                                         "alignment": "Right",
#                                                                         "tbl_name": "rt_ar_dly_bal_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "avail_bal",
#                                                                         "seq_order": 5,
#                                                                         "data_type": "decimal",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_ar_dly_bal_dp_rd_avail_bal",
#                                                                         "alignment": "Right",
#                                                                         "tbl_name": "rt_ar_dly_bal_dp_rd",
#                                                                         "validValueConfig": {
#                                                                                       "column_name": "Available Bal",
#                                                                                       "DataID": "rt_ar_dly_bal_dp_rd_avail_bal",
#                                                                                       "rpt_sp_param_name": "P_avail_bal",
#                                                                                       "sequence_order": 1,
#                                                                                       "filter_type": "text",
#                                                                                       "fltr_oprtr": "=",
#                                                                                       "field": "avail_bal"
#                                                                         }
#                                                           },
#                                                           {
#                                                                         "column_name": "rtd_grace_end_date",
#                                                                         "seq_order": 6,
#                                                                         "data_type": "date",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_rtd_grace_end_date",
#                                                                         "alignment": "Center",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "csi_code",
#                                                                         "seq_order": 7,
#                                                                         "data_type": "string",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_csi_code",
#                                                                         "alignment": "Left",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "abdcs_auf_lmt_exp_date",
#                                                                         "seq_order": 8,
#                                                                         "data_type": "date",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_abdcs_auf_lmt_exp_date",
#                                                                         "alignment": "Center",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "apacs_fund_owner",
#                                                                         "seq_order": 9,
#                                                                         "data_type": "string",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_apacs_fund_owner",
#                                                                         "alignment": "Left",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "apd_name",
#                                                                         "seq_order": 10,
#                                                                         "data_type": "string",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_apd_name",
#                                                                         "alignment": "Left",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "apd_code",
#                                                                         "seq_order": 11,
#                                                                         "data_type": "string",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_apd_code",
#                                                                         "alignment": "Left",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {
#                                                                                       "column_name": "Product Code",
#                                                                                       "DataID": "rt_apd_ar_mstr_dp_rd_apd_code",
#                                                                                       "rpt_sp_param_name": "P_apd_code",
#                                                                                       "sequence_order": 2,
#                                                                                       "filter_type": "text",
#                                                                                       "fltr_oprtr": "=",
#                                                                                       "field": "apd_code"
#                                                                         }
#                                                           },
#                                                           {
#                                                                         "column_name": "enart_value",
#                                                                         "seq_order": 12,
#                                                                         "data_type": "string",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_enart_value",
#                                                                         "alignment": "Left",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "frst_dpst_efctv_date",
#                                                                         "seq_order": 13,
#                                                                         "data_type": "date",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_frst_dpst_efctv_date",
#                                                                         "alignment": "Center",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           }
#                                            ]
import paramiko
nbytes = 4096
command = 'cat /data1/ui/igen/ruf-api-dev/logger_ser.log'
ssh = paramiko.Transport(('vlmazrasdev1ap1.fisdev.local', 22))
ssh.connect(username='uiadmin', password='Enchanting@459')
stdout_data = []
stderr_data = []
session = ssh.open_channel(kind='session')
session.exec_command(command)
while True:
    if session.recv_ready():
        stdout_data.append(session.recv(nbytes))
    if session.recv_stderr_ready():
        stderr_data.append(session.recv_stderr(nbytes))
    if session.exit_status_ready():
        break
print(stdout_data)
# sftp = ssh.open_sftp()
# log = sftp.open('/data1/ui/igen/ruf-api-dev/logger_ser.log')
# try:
#     for line in log:
#         print(line)
# finally:
#     log.close()

# # import pandas as pd
# # #
# # # res = []
# # # df = pd.read_json("C:\\Users\\e5567006\\Documents\\workspace\\ruf-api\\util\\15.json")
# # # columns = list(df.columns.values)
# # # col_dtypes = list(df.dtypes.values)
# # # for index, col in enumerate(columns):
# # #     dObj = {}
# # #     dObj['field'] = col
# # #     dObj['enableRowGroup'] = True
# # #     dObj['sortable'] = True
# # #     res.append(dObj)
# # # return res
# #
# # # def get_cat_recon(user_id, rpt_id, fe_id, filterData, prod_line, user_spec, fe_int_id, prod_grp):
# # #     output = {}
# # #     detail_col_lst = []
# # #     res = {}
# # #     list_of_files = glob.glob(DIR + rpt_id + '*.csv') # * means all if need specific format then *.csv
# # #     f_name = max(list_of_files, key=os.path.getctime)
# # #     df_rec = pd.read_csv(f_name)
# # #     locale = user_spec['locale'].replace("-", "_")
# # #     def format_curr(x):
# # #         try:
# # #             return format_currency(x, '', locale=locale)
# # #         except Exception as e:
# # #             return ""
# # #     for column in list(df_rec.select_dtypes(['float64']).columns):
# # #         df_rec[column] = df_rec[column].apply(lambda x :format_curr(x))
# # #     data_head = list(df_rec.columns.values)
# # #     format_type = str(get_format_type(rpt_id, fe_id, fe_int_id))
# # #     rpt_col = get_cat1_headers(rpt_id, fe_id, fe_int_id)
# # #     if len(rpt_col) < 0:
# # #         raise Exception(constants.RptHeaderErr, "Headers len(0)")
# # #     alignment = {}
# # #     data_typ = {}
# # #     pdf_conf = {}
# # #     data_len = {}
# # #     for col in rpt_col:
# # #         alignment[col.clmn_nme] = col.alignment
# # #         data_typ[col.clmn_nme] = col.data_typ
# # #         data_len[col.clmn_nme] = col.data_len
# # #     col_def = handler.HeadersUtil().convert_headers(rpt_col)
# # #     for cl in col_def:
# # #         detail_col_lst.append(cl['field'])
# # #         cl['enableRowGroup'] = True
# # #         if cl['data_type'].lower() == 'numeric':
# # #             cl['enableValue'] = True
# # #     pdf_conf['alignMent'] = alignment
# # #     pdf_conf['data_type'] = data_typ
# # #     pdf_conf['data_length'] = data_len
# # #     output['pdf_conf'] = pdf_conf
# # #     output['columnDef'] = col_def
# # #     output['columnValue'] = json.loads(df_rec.to_json(orient='records'))
# # #     res['detail'] = output
# # #     rpt_maint = get_rpt_by_id(rpt_id, fe_id, fe_int_id)
# # #     #try:
# # #         #if 0 < len(rpt_maint) < 2:
# # #             #res['report_note'] = rpt_maint[0].rpt_notes
# # #     #except Exception as e:
# # #         #raise Exception(constants.RptMaintErr, e)
# # #     res['cat'] = format_type.lower()
# # #     return res
# #
# # # import pandas as pd
# # # import tabula
# # # import pdfkit
# # # file_path = "C:\\Users\\e5567006\\Desktop\\ac027114.pdf"
# # #
# # # #"https://github.com/chezou/tabula-py/raw/master/tests/resources/data.pdf"#
# # #
# # # # df = tabula.read_pdf(file_path, encoding='utf-8', pages='3')
# # # # d = pdfkit.
# # # # import PyPDF2
# # # # # file = open(file_path, 'rb')
# # # # # file_r = PyPDF2.PdfFileReader(file)
# # # # #
# # # import textract
# # #
# # # d = textract.process("C:\\Users\\e5567006\\Desktop\\ac027114.pdf")
# #
# # # import itertools
# # # import threading
# # # import time
# # # import sys
# # #
# # # done = False
# # # #here is the animation
# # # def animate():
# # #     for c in itertools.cycle(['|', '/', '-', '\\']):
# # #         if done:
# # #             break
# # #         sys.stdout.write('\rloading ' + c)
# # #         sys.stdout.flush()
# # #         time.sleep(0.1)
# # #     sys.stdout.write('\rDone!     ')
# # #
# # # t = threading.Thread(target=animate)
# # # t.start()
# # #
# # # #long process here
# # # time.sleep(10)
# # # done = True
# #
# # import ply.lex as lex, re
# #
# # tokens = (
# #     "TABLE",
# #     "JOIN",
# #     "COLUMN",
# #     "TRASH"
# # )
# #
# # tables = {"tables": {}, "alias": {}}
# # columns = []
# #
# # t_TRASH = r"Select|on|=|;|\s+|,|\t|\r"
# #
# # def t_TABLE(t):
# #     r"from\s(\w+)\sas\s(\w+)"
# #
# #     regex = re.compile(t_TABLE.__doc__)
# #     m = regex.search(t.value)
# #     if m is not None:
# #         tbl = m.group(1)
# #         alias = m.group(2)
# #         tables["tables"][tbl] = ""
# #         tables["alias"][alias] = tbl
# #
# #     return t
# #
# # def t_JOIN(t):
# #     r"inner\s+join\s+(\w+)\s+as\s+(\w+)"
# #
# #     regex = re.compile(t_JOIN.__doc__)
# #     m = regex.search(t.value)
# #     if m is not None:
# #         tbl = m.group(1)
# #         alias = m.group(2)
# #         tables["tables"][tbl] = ""
# #         tables["alias"][alias] = tbl
# #     return t
# #
# # def t_COLUMN(t):
# #     r"(\w+\.\w+)"
# #
# #     regex = re.compile(t_COLUMN.__doc__)
# #     m = regex.search(t.value)
# #     if m is not None:
# #         t.value = m.group(1)
# #         columns.append(t.value)
# #     return t
# #
# # def t_error(t):
# #     raise TypeError("Unknown text '%s'" % (t.value,))
# #     t.lexer.skip(len(t.value))
# #
# # # here is where the magic starts
# # # def mylex(inp):
# # #     lexer = lex.lex()
# # #     lexer.input(inp)
# # #
# # #     for token in lexer:
# # #         pass
# # #
# # #     result = {}
# # #     for col in columns:
# # #         tbl, c = col.split('.')
# # #         if tbl in tables["alias"].keys():
# # #             key = tables["alias"][tbl]
# # #         else:
# # #             key = tbl
# # #
# # #         if key in result:
# # #             result[key].append(c)
# # #         else:
# # #             result[key] = list()
# # #             result[key].append(c)
# # #
# # #     print(result)
# # #     # {'tb1': ['col1', 'col7'], 'tb2': ['col2', 'col8']}
# # #
# # # string = "Select a.col1, b.col2 from tb1 as a inner join tb2 as b on tb1.col7 = tb2.col8;"
# # # mylex(string)
# import re
#
#
# st = "sdfsdfsdf10fdsfsdfd1111vdsfsdf0000fsdfsd11"
# st.isdigit()
# print(''.join([l for l in list(st) if l.isdigit()]))
#
# # re.findall()
# print("".join(sorted((''.join(i for i in "sdfsdfsdf10fdsfsdfd1111vdsfsdf0000fsdfsd11" if i.isdigit())), reverse=True)))


data = {
              "columnDef": [{
                                           "field": "rtd_crrnt_mtrty_amt",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_rtd_crrnt_mtrty_amt",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Cur Mat Amt",
                                           "data_type": "decimal",
                                           "allowedAggFuncs": [
                                                          "avg",
                                                          "count",
                                                          "sum",
                                                          "max",
                                                          "min"
                                           ],
                                           "enableRowGroup": True,
                                           "sortable": True,
                                           "isNum": True
                             },
                             {
                                           "field": "full_date_txt",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_full_date_txt",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Booking Date",
                                           "data_type": "date",
                                           "enableRowGroup": True,
                                           "sortable": True
                             },
                             {
                                           "field": "ar_id_item",
                                           "DataID": "rt_ar_dly_bal_dp_rd_ar_id_item",
                                           "tbl_name": "rt_ar_dly_bal_dp_rd",
                                           "headerName": "Acct #",
                                           "data_type": "string",
                                           "enableRowGroup": True,
                                           "sortable": True
                             },
                             {
                                           "field": "ldgr_bal",
                                           "DataID": "rt_ar_dly_bal_dp_rd_ldgr_bal",
                                           "tbl_name": "rt_ar_dly_bal_dp_rd",
                                           "headerName": "Ledger Bal",
                                           "data_type": "decimal",
                                           "enableRowGroup": True,
                                           "sortable": True,
                                           "isNum": True
                             },
                             {
                                           "field": "avail_bal",
                                           "DataID": "rt_ar_dly_bal_dp_rd_avail_bal",
                                           "tbl_name": "rt_ar_dly_bal_dp_rd",
                                           "headerName": "Available Bal",
                                           "data_type": "decimal",
                                           "enableRowGroup": True,
                                           "sortable": True,
                                           "isNum": True,
                                           "operator": "="
                             },
                             {
                                           "field": "rtd_grace_end_date",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_rtd_grace_end_date",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Grace End Date",
                                           "data_type": "date",
                                           "enableRowGroup": True,
                                           "sortable": True
                             },
                             {
                                           "field": "csi_code",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_csi_code",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Instruction Code",
                                           "data_type": "string",
                                           "enableRowGroup": True,
                                           "sortable": True
                             },
                             {
                                           "field": "abdcs_auf_lmt_exp_date",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_abdcs_auf_lmt_exp_date",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Expiry Date",
                                           "data_type": "date",
                                           "enableRowGroup": True,
                                           "sortable": True
                             },
                             {
                                           "field": "apacs_fund_owner",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_apacs_fund_owner",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Fund Owner",
                                           "data_type": "string",
                                           "enableRowGroup": True,
                                           "sortable": True
                             },
                             {
                                           "field": "apd_name",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_apd_name",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Product Name",
                                           "data_type": "string",
                                           "enableRowGroup": True,
                                           "sortable": True
                             },
                             {
                                           "field": "apd_code",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_apd_code",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Product Code",
                                           "data_type": "string",
                                           "enableRowGroup": True,
                                           "sortable": True,
                                           "operator": "="
                             },
                             {
                                           "field": "enart_value",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_enart_value",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Ent Acct Type",
                                           "data_type": "string",
                                           "enableRowGroup": True,
                                           "sortable": True
                             },
                             {
                                           "field": "frst_dpst_efctv_date",
                                           "DataID": "rt_apd_ar_mstr_dp_rd_frst_dpst_efctv_date",
                                           "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                           "headerName": "Effective Date",
                                           "data_type": "date",
                                           "enableRowGroup": True,
                                           "sortable": True
                             }
              ],
              "filters": {
                             "condition": "and",
                             "rules": [{
                                                          "field": "avail_bal",
                                                          "operator": "=",
                                                          "entity": "IGNxxx",
                                                          "tableID": "",
                                                          "data_type": "decimal",
                                                          "DataID": "rt_ar_dly_bal_dp_rd_avail_bal",
                                                          "value": "60"
                                           },
                                           {
                                                          "field": "apd_code",
                                                          "operator": "=",
                                                          "entity": "IGNxxx",
                                                          "tableID": "",
                                                          "data_type": "string",
                                                          "DataID": "rt_apd_ar_mstr_dp_rd_apd_code",
                                                          "value": "MMDA"
                                           }
                             ]
              },
              "isTable": False,
              "is_ui_based": False,
              "newRptID": "IGNxxx",
              "prod_line": "RD",
              "query": "select RT_APD_AR_MSTR_DP_RD.RTD_CRRNT_MTRTY_AMT,RT_APD_AR_MSTR_DP_RD.FULL_DATE_TXT,RT_AR_DLY_BAL_DP_RD.AR_ID_ITEM,RT_AR_DLY_BAL_DP_RD.LDGR_BAL,RT_AR_DLY_BAL_DP_RD.AVAIL_BAL,RT_APD_AR_MSTR_DP_RD.RTD_GRACE_END_DATE,RT_APD_AR_MSTR_DP_RD.CSI_CODE,RT_APD_AR_MSTR_DP_RD.ABDCS_AUF_LMT_EXP_DATE,RT_APD_AR_MSTR_DP_RD.APACS_FUND_OWNER,RT_APD_AR_MSTR_DP_RD.APD_NAME,RT_APD_AR_MSTR_DP_RD.APD_CODE,RT_APD_AR_MSTR_DP_RD.ENART_VALUE,RT_APD_AR_MSTR_DP_RD.FRST_DPST_EFCTV_DATE from RT_APD_AR_MSTR_DP_RD left join RT_AR_DLY_BAL_DP_RD on RT_APD_AR_MSTR_DP_RD.ar_id_item=RT_AR_DLY_BAL_DP_RD.ar_id_item and RT_APD_AR_MSTR_DP_RD.ldbid=RT_AR_DLY_BAL_DP_RD.ldbid",
              "conn_method": "hive",
              "params": {
                             "startRow": 0,
                             "endRow": 99,
                             "rowGroupCols": [{
                                           "id": "ar_id_item",
                                           "displayName": "Acct #",
                                           "field": "ar_id_item"
                             }],
                             "valueCols": [{
                                           "id": "avail_bal",
                                           "aggFunc": "sum",
                                           "displayName": "Available Bal",
                                           "field": "avail_bal"
                             }],
                             "pivotCols": [],
                             "pivotMode": False,
                             "groupKeys": [],
                             "filterModel": {},
                             "sortModel": []
              },
              "cacheCode": "c21a076e-2a82-4619-8f20-7a0d992fa82f",
              "editFlag": False,
              "columns": [{
                                           "tab": "detail",
                                           "tab_title": "Details",
                                           "data": [{
                                                                        "column_name": "rtd_crrnt_mtrty_amt",
                                                                        "seq_order": 1,
                                                                        "data_type": "decimal",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_rtd_crrnt_mtrty_amt",
                                                                        "alignment": "Right",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "full_date_txt",
                                                                        "seq_order": 2,
                                                                        "data_type": "date",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_full_date_txt",
                                                                        "alignment": "Center",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "ar_id_item",
                                                                        "seq_order": 3,
                                                                        "data_type": "string",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_ar_dly_bal_dp_rd_ar_id_item",
                                                                        "alignment": "Left",
                                                                        "tbl_name": "rt_ar_dly_bal_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "ldgr_bal",
                                                                        "seq_order": 4,
                                                                        "data_type": "decimal",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_ar_dly_bal_dp_rd_ldgr_bal",
                                                                        "alignment": "Right",
                                                                        "tbl_name": "rt_ar_dly_bal_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "avail_bal",
                                                                        "seq_order": 5,
                                                                        "data_type": "decimal",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_ar_dly_bal_dp_rd_avail_bal",
                                                                        "alignment": "Right",
                                                                        "tbl_name": "rt_ar_dly_bal_dp_rd",
                                                                        "validValueConfig": {
                                                                                      "column_name": "Available Bal",
                                                                                      "DataID": "rt_ar_dly_bal_dp_rd_avail_bal",
                                                                                      "rpt_sp_param_name": "P_avail_bal",
                                                                                      "sequence_order": 1,
                                                                                      "filter_type": "text",
                                                                                      "fltr_oprtr": "=",
                                                                                      "field": "avail_bal"
                                                                        }
                                                          },
                                                          {
                                                                        "column_name": "rtd_grace_end_date",
                                                                        "seq_order": 6,
                                                                        "data_type": "date",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_rtd_grace_end_date",
                                                                        "alignment": "Center",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "csi_code",
                                                                        "seq_order": 7,
                                                                        "data_type": "string",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_csi_code",
                                                                        "alignment": "Left",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "abdcs_auf_lmt_exp_date",
                                                                        "seq_order": 8,
                                                                        "data_type": "date",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_abdcs_auf_lmt_exp_date",
                                                                        "alignment": "Center",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "apacs_fund_owner",
                                                                        "seq_order": 9,
                                                                        "data_type": "string",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_apacs_fund_owner",
                                                                        "alignment": "Left",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "apd_name",
                                                                        "seq_order": 10,
                                                                        "data_type": "string",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_apd_name",
                                                                        "alignment": "Left",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "apd_code",
                                                                        "seq_order": 11,
                                                                        "data_type": "string",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_apd_code",
                                                                        "alignment": "Left",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {
                                                                                      "column_name": "Product Code",
                                                                                      "DataID": "rt_apd_ar_mstr_dp_rd_apd_code",
                                                                                      "rpt_sp_param_name": "P_apd_code",
                                                                                      "sequence_order": 2,
                                                                                      "filter_type": "text",
                                                                                      "fltr_oprtr": "=",
                                                                                      "field": "apd_code"
                                                                        }
                                                          },
                                                          {
                                                                        "column_name": "enart_value",
                                                                        "seq_order": 12,
                                                                        "data_type": "string",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_enart_value",
                                                                        "alignment": "Left",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "frst_dpst_efctv_date",
                                                                        "seq_order": 13,
                                                                        "data_type": "date",
                                                                        "isGrp": False,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_apd_ar_mstr_dp_rd_frst_dpst_efctv_date",
                                                                        "alignment": "Center",
                                                                        "tbl_name": "rt_apd_ar_mstr_dp_rd",
                                                                        "validValueConfig": {}
                                                          }
                                           ]
                             },
                             {
                                           "tab": "summary",
                                           "tab_title": "Sum of Ledger Bal",
                                           "data": [{
                                                                        "column_name": "ar_id_item",
                                                                        "seq_order": 1,
                                                                        "data_type": "string",
                                                                        "isGrp": True,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_ar_dly_bal_dp_rd_ar_id_item",
                                                                        "alignment": "Left",
                                                                        "tbl_name": "rt_ar_dly_bal_dp_rd",
                                                                        "is_grp": "Y",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "ldgr_bal",
                                                                        "seq_order": 2,
                                                                        "data_type": "decimal",
                                                                        "isGrp": False,
                                                                        "aggFunc": "sum",
                                                                        "column_width": "200",
                                                                        "DataID": "rt_ar_dly_bal_dp_rd_ldgr_bal",
                                                                        "alignment": "Right",
                                                                        "tbl_name": "rt_ar_dly_bal_dp_rd",
                                                                        "is_grp": "N",
                                                                        "validValueConfig": {}
                                                          }
                                           ]
                             },
                             {
                                           "tab": "summary",
                                           "tab_title": "Sum of Available Bal",
                                           "data": [{
                                                                        "column_name": "ar_id_item",
                                                                        "seq_order": 1,
                                                                        "data_type": "string",
                                                                        "isGrp": True,
                                                                        "aggFunc": None,
                                                                        "column_width": "200",
                                                                        "DataID": "rt_ar_dly_bal_dp_rd_ar_id_item",
                                                                        "alignment": "Left",
                                                                        "tbl_name": "rt_ar_dly_bal_dp_rd",
                                                                        "is_grp": "Y",
                                                                        "validValueConfig": {}
                                                          },
                                                          {
                                                                        "column_name": "avail_bal",
                                                                        "seq_order": 2,
                                                                        "data_type": "decimal",
                                                                        "isGrp": False,
                                                                        "aggFunc": "sum",
                                                                        "column_width": "200",
                                                                        "DataID": "rt_ar_dly_bal_dp_rd_avail_bal",
                                                                        "alignment": "Right",
                                                                        "tbl_name": "rt_ar_dly_bal_dp_rd",
                                                                        "is_grp": "N",
                                                                        "validValueConfig": {
                                                                                      "column_name": "Available Bal",
                                                                                      "DataID": "rt_ar_dly_bal_dp_rd_avail_bal",
                                                                                      "rpt_sp_param_name": "P_avail_bal",
                                                                                      "sequence_order": 1,
                                                                                      "filter_type": "text",
                                                                                      "fltr_oprtr": "=",
                                                                                      "field": "avail_bal"
                                                                        }
                                                          }
                                           ]
                             }
              ],
              "max_sum_cols": 2,
              "sav_rpt": {
                             "name": "Multitab_join_11",
                             "cat": "TXN",
                             "desc": "A query based multitab join with aggregations",
                             "downloadType": "PDF,EXCEL,TXT",
                             "configuration": "Header,Footer",
                             "connectivity": "hive",
                             "reportFormat": "MultiTab"
              }
}


# data['columns']['data']

# temp_lst = [j['data'] for j in [i for i in data['columns'] if i['tab'] != "detail"]]

# print(temp_lst)

# for i in range(lentemp_lst:
#     for j in temp_lst

# for i in range(len(temp_lst) - 1):
#     for data in range(len(sum.data) - 1):
#         pass

# js = [
#     {
#                                                                         "column_name": "rtd_crrnt_mtrty_amt",
#                                                                         "seq_order": 1,
#                                                                         "data_type": "decimal",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_rtd_crrnt_mtrty_amt",
#                                                                         "alignment": "Right",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "full_date_txt",
#                                                                         "seq_order": 2,
#                                                                         "data_type": "date",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_full_date_txt",
#                                                                         "alignment": "Center",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "ar_id_item",
#                                                                         "seq_order": 3,
#                                                                         "data_type": "string",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_ar_dly_bal_dp_rd_ar_id_item",
#                                                                         "alignment": "Left",
#                                                                         "tbl_name": "rt_ar_dly_bal_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "ldgr_bal",
#                                                                         "seq_order": 4,
#                                                                         "data_type": "decimal",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_ar_dly_bal_dp_rd_ldgr_bal",
#                                                                         "alignment": "Right",
#                                                                         "tbl_name": "rt_ar_dly_bal_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "avail_bal",
#                                                                         "seq_order": 5,
#                                                                         "data_type": "decimal",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_ar_dly_bal_dp_rd_avail_bal",
#                                                                         "alignment": "Right",
#                                                                         "tbl_name": "rt_ar_dly_bal_dp_rd",
#                                                                         "validValueConfig": {
#                                                                                       "column_name": "Available Bal",
#                                                                                       "DataID": "rt_ar_dly_bal_dp_rd_avail_bal",
#                                                                                       "rpt_sp_param_name": "P_avail_bal",
#                                                                                       "sequence_order": 1,
#                                                                                       "filter_type": "text",
#                                                                                       "fltr_oprtr": "=",
#                                                                                       "field": "avail_bal"
#                                                                         }
#                                                           },
#                                                           {
#                                                                         "column_name": "rtd_grace_end_date",
#                                                                         "seq_order": 6,
#                                                                         "data_type": "date",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_rtd_grace_end_date",
#                                                                         "alignment": "Center",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "csi_code",
#                                                                         "seq_order": 7,
#                                                                         "data_type": "string",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_csi_code",
#                                                                         "alignment": "Left",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "abdcs_auf_lmt_exp_date",
#                                                                         "seq_order": 8,
#                                                                         "data_type": "date",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_abdcs_auf_lmt_exp_date",
#                                                                         "alignment": "Center",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "apacs_fund_owner",
#                                                                         "seq_order": 9,
#                                                                         "data_type": "string",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_apacs_fund_owner",
#                                                                         "alignment": "Left",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "apd_name",
#                                                                         "seq_order": 10,
#                                                                         "data_type": "string",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_apd_name",
#                                                                         "alignment": "Left",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "apd_code",
#                                                                         "seq_order": 11,
#                                                                         "data_type": "string",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_apd_code",
#                                                                         "alignment": "Left",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {
#                                                                                       "column_name": "Product Code",
#                                                                                       "DataID": "rt_apd_ar_mstr_dp_rd_apd_code",
#                                                                                       "rpt_sp_param_name": "P_apd_code",
#                                                                                       "sequence_order": 2,
#                                                                                       "filter_type": "text",
#                                                                                       "fltr_oprtr": "=",
#                                                                                       "field": "apd_code"
#                                                                         }
#                                                           },
#                                                           {
#                                                                         "column_name": "enart_value",
#                                                                         "seq_order": 12,
#                                                                         "data_type": "string",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_enart_value",
#                                                                         "alignment": "Left",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           },
#                                                           {
#                                                                         "column_name": "frst_dpst_efctv_date",
#                                                                         "seq_order": 13,
#                                                                         "data_type": "date",
#                                                                         "isGrp": False,
#                                                                         "aggFunc": None,
#                                                                         "column_width": "200",
#                                                                         "DataID": "rt_apd_ar_mstr_dp_rd_frst_dpst_efctv_date",
#                                                                         "alignment": "Center",
#                                                                         "tbl_name": "rt_apd_ar_mstr_dp_rd",
#                                                                         "validValueConfig": {}
#                                                           }
#                                            ]
import paramiko
nbytes = 4096
command = 'cat /data1/ui/igen/ruf-api-dev/logger_ser.log'
ssh = paramiko.Transport(('vlmazrasdev1ap1.fisdev.local', 22))
ssh.connect(username='uiadmin', password='Enchanting@459')
stdout_data = []
stderr_data = []
session = ssh.open_channel(kind='session')
session.exec_command(command)
while True:
    if session.recv_ready():
        stdout_data.append(session.recv(nbytes))
    if session.recv_stderr_ready():
        stderr_data.append(session.recv_stderr(nbytes))
    if session.exit_status_ready():
        break
print(stdout_data)
# sftp = ssh.open_sftp()
# log = sftp.open('/data1/ui/igen/ruf-api-dev/logger_ser.log')
# try:
#     for line in log:
#         print(line)
# finally:
#     log.close()

