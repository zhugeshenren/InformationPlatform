
/*
* 将从服务器上传过来的list转换为字典
* 约定数据格式为
* list[tuple,tuple....]
* list[0] : 约定存储列的名称
* */
function ListToDict(listData) {

    var result = null;
    if(listData == null || listData.length <= 0)
        return result;

    var keySet = listData[0];
    result = [];

    for(var i=1;i<listData.length;i++){
        tdict = {};
        for (var j =0;j<keySet.length;j++){
            tdict[keySet[j]] = listData[i][j];
        }
        result.push(tdict)
    }
    return result;
}