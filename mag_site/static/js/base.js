AOS.init();

// ScrollReveal().reveal('.container'); 
document.addEventListener("DOMContentLoaded", function(){
    // make it as accordion for smaller screens
    if (window.innerWidth > 992) {
        document.querySelectorAll('.navbar .nav-item').forEach(function(everyitem){
            everyitem.addEventListener('mouseover', function(e){
                let el_link = this.querySelector('a[data-bs-toggle]');
                if(el_link != null){
                    let nextEl = el_link.nextElementSibling;
                    el_link.classList.add('show');
                    nextEl.classList.add('show');
                }
            });
            everyitem.addEventListener('mouseleave', function(e){
                let el_link = this.querySelector('a[data-bs-toggle]');

                if(el_link != null){
                    let nextEl = el_link.nextElementSibling;
                    el_link.classList.remove('show');
                    nextEl.classList.remove('show');
                }
            })
        }); }
    // end if innerWidth
    }); 


    /////////////////////////////////////////////////
    
        let latesturl = "/api/latest/home/post/v1/?lang={{lang}}"
    
        //================================================================
        var requestOptions = {
                method: 'GET',
                redirect: 'follow'
                };
                fetch(latesturl, requestOptions)
                .then(response => response.json())
                .then(result => {
                    //GETTING LATEST POST
                        latesturl = result['links']['next']
                        myArray = result['results']
                        myArray.forEach(function (p) {
                            let mystring = p.intro
                            let mobile = mystring.substring(0,35);
                            let desktop = mystring.substring(0,150);
                            
                            document.getElementById("homeLatestPost").innerHTML += `
                            <div data-aos="fade-down-left" class="col-12 mb-1 " >
                        <div class="card border-0">
                            <a href="${p.get_absolute_url}" class="text-decoration-none text-dark">
                                <div class="card-body d-flex">
                                <div >
                                    <img style="width: 150px; height: 100px; object-fit: cover;" src="${p.intro_image}" alt="this is image">
                                </div>
    
                                <div style="margin-left: 10px;">
                                    <p>${p.title}</p>
                                    <div class="">
                                        <p class="d-none d-md-block">
                                            ${desktop}
                                        </p>
                                        <p class="d-block d-md-none">
                                            ${mobile}
                                        </p>
                                        <span class="text-info">Read more<i class="uil uil-arrow-right"></i></span>
                                    </div>
                                    
                                </div>
                                </div>
                            </a>
                        </div>
                        </div>                        
                            `     
                        });
                        if (result['links']['next'] == null){
                            document.getElementById("lsfetch-button").classList.add("d-none");
                        }
                })
                .catch(error => console.log('error', error));

        // //===========================================================================
        function lmyFunction() {

                fetch(latesturl, requestOptions)
                .then(response => response.json())
                .then(result => {
                        latesturl = result['links']['next']
                        myArray = result['results']
                        myArray.forEach(function (p) {
                            let mystring = p.intro
                            let mobile = mystring.substring(0,35);
                            let desktop = mystring.substring(0,150);
                            
                            document.getElementById("homeLatestPost").innerHTML += `

                            <div data-aos="fade-down-left" class="col-12 mb-1 " >
                        <div class="card border-0">
                            <a href="${p.get_absolute_url}" class="text-decoration-none text-dark">
                                <div class="card-body d-flex">
                                <div >
                                    <img style="width: 150px; height: 100px; object-fit: cover;" src="${p.intro_image}" alt="this is image">
                                </div>
    
                                <div style="margin-left: 10px;">
                                    <p>${p.title}</p>
                                    <div class="">
                                        <p class="d-none d-md-block">
                                        ${desktop}
                                        </p>
                                        <p class="d-block d-md-none">
                                        ${mobile}
                                        </p>
                                        <span class="text-info">Read more<i class="uil uil-arrow-right"></i></span>
                                    </div>
                                    
                                </div>
                                </div>
                            </a>
                        </div>
                 </div>

                            `    
                        });
                        if (result['links']['next'] == null){
                    
                            document.getElementById("lsfetch-button").classList.add("d-none");
                        }
                })
                .catch(error => console.log('error', error));


            }