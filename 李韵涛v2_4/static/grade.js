function checkgrade(){
    let stu_sn = document.querySelector(".stu_sn");
    let cou_sn = document.querySelector(".cou_sn");
    let checkgradebtn = document.querySelector(".checkgradebtn");
    stu_sn.onchange = (e) => {
    checkgradebtn.outerHTML = `<a href="/grade/check/${stu_sn.value}/${1}" class = 'checkgradebtn' >查询成绩</a>`;
    }
    cou_sn.onchange = (e) => {
        let checkgradebtn = document.querySelector(".checkgradebtn");
        checkgradebtn.outerHTML = `<a href="/grade/check/${stu_sn.value}/${cou_sn.value}" class = 'checkgradebtn' >查询成绩</a>`;
        }
}
checkgrade();