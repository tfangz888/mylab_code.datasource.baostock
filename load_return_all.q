path:`$":/home/toby/data/datasource/baostock/daily"
files:key path / 所有文件

/ returnday:([date:`date$(); sym:`symbol$()];open:`float$();high:`float$();low:`float$();close:`float$();preclose:`float$(); volume:`long$();amount:`float$()) 
/ loadFile: {[path;file]d:("DSFFFFFJF";enlist ",") 0: ` sv path,file;t:select date, sym:code, open, high, low, close, preclose, volume, amount from d}
returnday:([date:`date$(); sym:`symbol$()];return:`float$(); amount:`float$()) 
loadFile: {[path;file]d:("DSFFFFFJF";enlist ",") 0: ` sv path,file;t:select date, sym:code, return:100* log close % preclose, amount from d}

`returnday upsert raze loadFile[path] each files

codes: `#exec distinct sym from returnday / 从table中取得所有的symbol

