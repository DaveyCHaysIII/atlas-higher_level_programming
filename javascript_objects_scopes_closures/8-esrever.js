exports.esrever = function (list) {
    let newList = [];
    for (let i = list.length; i > 0; i--) {
        newList.push(list[i]);
    }
    return newList;
}
