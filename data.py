l=["Dr. Poonkuntran S",
"Dr. Pon Harshavardhanan",
"Dr. Pushpinder Singh Patheja",
"Dr. M. Suresh",
"Dr. Hemant Kumar Nashin",
"Dr. Sheetal Sharma",
"Dr. Prasad Begde",
"Dr. Siddhartha Maiti",
"Dr. S. Balaguru"]

s=["Executive Dean, VIT Bhopal",
"Dean-SCAI, VIT Bhopal University",
"Dean-SCOPE, VIT Bhopal University",
"Dean SEEE, VIT Bhopal",
"Dean SASL, VIT Bhopal",
"Dean SOA, VIT Bhopal",
"Dean, VIT-BS",
"SBET, VIT Bhopal",
"Dean, SMEC, VIT Bhopal"]

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
