l=["Dr. Rajdeep Singh Payal",
"Dr. Saurav Prasad",
"Dr. Sayed Mohammed Zeeshan",
"Dr. Siddhartha Maiti",
"Dr. Soumya Sankar Ghosh",
"Dr. Shiv Manjaree Gopaliya"]

s=["SASL, VIT Bhopal University",
"SASL, VIT Bhopal University",
"SASL, VIT Bhopal University",
"SBET, VIT Bhopal University",
"SASL, VIT Bhopal University",
"SMEC, VIT Bhopal University"]

for i in range(len(l)):
    print(f'''
                        <div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.1s">
                            <div class="team-item bg-light">
                                <!-- <div class="overflow-hidden">
                                    <img class="img-fluid" src="images/committee/Buyya.jpg" alt="">
                                </div> -->
                                <div class="text-center p-4">
                                    <h5 class="mb-0">{l[i]}</h5>
                                    <small>{s[i]}</small>
                                </div>
                            </div>
                        </div>
                        ''')
