document.addEventListener("DOMContentLoaded",()=>{let e=document.querySelectorAll(".my-slide"),t=0;function l(){e[t].classList.remove("my-active"),e[t=(t+1)%e.length].classList.add("my-active")}e.length>0&&setInterval(l,3e3);let s=document.querySelectorAll(".why-us-img"),i=0;function a(){s[i].classList.remove("active"),s[i=(i+1)%s.length].classList.add("active")}s.length>0&&setInterval(a,6e3)});