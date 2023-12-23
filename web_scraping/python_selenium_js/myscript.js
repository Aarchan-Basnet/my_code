//to js obj
titles = document.querySelector('thead').childNodes[0].innerText.split('\t');
trows = document.querySelector('tbody').children;

array = {};
for (i=0; i<trows.length;i++){
    obj = {};
    final_obj = {};
    keys = titles;
    vals = trows[i];
    values = vals.innerText.split('\t');
    keys.forEach((element, index) => {obj[element] = values[index];});
    new_key = obj["Symbol "];
    delete obj["Symbol "] ;
    delete obj.SN;
    final_obj[new_key] = obj;
    Object.assign(array, final_obj);
    console.log(array);
}

//download json file
json = JSON.stringify(array);
json = [json];
        var blob1 = new Blob(json, { type: "text/plain;charset=utf-8" });
 
        //Check the Browser.
        var isIE = false || !!document.documentMode;
        if (isIE) {
            window.navigator.msSaveBlob(blob1, "Nepal_stock_today.json");
        } else {
            var url = window.URL || window.webkitURL;
            link = url.createObjectURL(blob1);
            var a = document.createElement("a");
            a.download = "Nepal_stock_today.json";
            a.href = link;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);}