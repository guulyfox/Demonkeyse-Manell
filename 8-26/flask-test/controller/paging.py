# -*- coding: utf-8 -*-
__author__ = 'wenyao'

import functools
from flask import request,current_app


def paging_warpper(default_pagesize=15,default_pagingkey=None):
    def paging_warpper_in(func):
        def warpper(*argv,**kw):
            result = func(*argv,**kw)
            #type_judge = any([isinstance(result['result'],list),all([isinstance(result['result'],dict),default_pagingkey])])
            #return type_judge
            if 'status' in result and result['status'] == 0 and any([isinstance(result['result'],list),all([isinstance(result['result'],dict),default_pagingkey])]) and 'nopage=1' not in request.url:
                pagesize = request.args.get('pagesize',default_pagesize,type=int)
                pagenum = request.args.get('pagenum',1,type=int)
                page_result = {}
                if default_pagingkey is None:
                    total = len(result['result']) 
                    page_result['items'] = result['result'][(pagenum-1)*pagesize:(pagenum)*pagesize]
                else:
                    total = len(result['result'][default_pagingkey])
                    page_result['items'] = result['result'][default_pagingkey][(pagenum-1)*pagesize:(pagenum)*pagesize]
                page_result.update({'total':total,'pagesize':pagesize,'pagenum':pagenum,'total_page':total/pagesize if total % pagesize == 0 else total/pagesize + 1})
                result['result'] = page_result
                return result
            return result
        return warpper
    return paging_warpper_in




