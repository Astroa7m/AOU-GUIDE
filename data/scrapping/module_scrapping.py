import csv

import requests
from bs4 import BeautifulSoup

# Sample HTML
html_content = """
<div id="ctl00_ctl50_g_b140d04d_c55f_489b_a897_9f8364e914ed_ctl00_dWebpart" class="wp-wrapper">

    <div>
        <div class="input-group mb-1 col-md-6">
			<div class="input-group-prepend">
                <button class="btn btn-success" type="button" id="btnClearSearchCourse">All Courses</button>
            </div>
            <input type="text" class="form-control" placeholder="Search By Course Code / Title..." aria-label="Search By Course Code / Title..." aria-describedby="basic-addon2" id="txtSearchCourse">
            <div class="input-group-append">
                <button class="btn btn-outline-secondary" type="button" id="btnSearchCourse"><i class="fa fa-search"></i></button>
            </div>
        </div>
    </div>

    

            <div class="course-item">
                <div class="course-title">
                    AR111&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Arabic Communication Skills (I) <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    AR111 is three credit hour university requirements. It aims to enable students to acquire the Arabic language skills needed at university level, specifically: Arabic syntactic structures, grammatical inflection and case ending in spoken and written Arabic, ability to read Arabic texts in different disciplines, adequate training in writing and using dictionary
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_75">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_75" class="modal fade" role="dialog" style="display: none;" aria-hidden="true">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Arabic Communication Skills (I)</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>AR111</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Arabic Communication Skills (I)</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>AR111 is three credit hour university requirements. It aims to enable students to acquire the Arabic language skills needed at university level, specifically: Arabic syntactic structures, grammatical inflection and case ending in spoken and written Arabic, ability to read Arabic texts in different disciplines, adequate training in writing and using dictionary</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    AR112&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Arabic Communication Skills (II) <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    AR112 is a three credit hour university requirement. It aims at developing students’ skills in text analysis and literary appreciation. Students are introduced to the principles of accurate pronunciation and sound reading of texts. The course also provides training in Arabic rhetoric and literary genres.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_76">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_76" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Arabic Communication Skills (II)</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>AR112</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Arabic Communication Skills (II)</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>AR111</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>AR112 is a three credit hour university requirement. It aims at developing students’ skills in text analysis and literary appreciation. Students are introduced to the principles of accurate pronunciation and sound reading of texts. The course also provides training in Arabic rhetoric and literary genres.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    B207-A&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Shaping Business Opportunities <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    B207A is an 8-credit (30 points), Level 5 UK-OU based course offered through the Business Program at the Arab Open University as a compulsory course for all students enrolled in all tracks in the program. Entry into this course is contingent upon the successful completion of BUS110. The B207 module in this new study plan is an OU updated version of its equivalent B203A module.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_9">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_9" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Shaping Business Opportunities</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B207-A</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Shaping Business Opportunities</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>B207A is an 8-credit (30 points), Level 5 UK-OU based course offered through the Business Program at the Arab Open University as a compulsory course for all students enrolled in all tracks in the program. Entry into this course is contingent upon the successful completion of BUS110. The B207 module in this new study plan is an OU updated version of its equivalent B203A module.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;&ZeroWidthSpace;</span><span class="ms-rteThemeFontFace-1" lang="EN-GB" style="font-size:13px;">This
module is designed to provide intermediate conceptual and practical learning to
students in operations management, marketing and human resource management. The
module comprises 16 study weeks (including final assessment).&nbsp;</span><br><br></span></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><p style="text-align:justify;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">At the end of the module, learners will be expected to:</span></p><ol style="text-align:justify;"><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Develop a critical appreciation of the interactions between various business functions (operations management, marketing and human resource management) and the integrative complexity that shapes business innovation.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Develop a critical understanding of why new products and services are imperative to contemporary business practice. Also to develop knowledge and understanding of external issues affecting the successful running of organizations, including how they compete in a global context.<br></span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Develop knowledge and understanding of the elements required to build long-term success in organizations, and how students can contribute to the fostering of long-term value creation.&ZeroWidthSpace;<br></span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">develop knowledge and critical understanding of the theories, concepts and models of different business functions (operations management, marketing and human resource management).</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">B. Cognitive skills</span></strong><br></span></p><p style="text-align:justify;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">At the end of the module learners will be expected to:</span></p><ol style="text-align:justify;"><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Select and<strong> </strong>critically analyse information relevant to a particular problem or issue related to business and management.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Evaluate and compare competing perspectives, theoretical models and concepts in the context of practical situations</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Gather and synthesise material from a variety of sources in constructing arguments applied to business and management&nbsp;&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br><br></span></p><p style="text-align:justify;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">At the end of the module, learners will be expected to:</span></p><ol style="text-align:justify;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Communicate in a professional manner in written work, face to face and online. Plan, monitor and review progress as independent learner, including a focus on personal skills development.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Develop an awareness of ethical issues and professional standards relevant to business and management</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong><br></span></p><p style="text-align:justify;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">At the end of the module, learners will be expected to:</span></p><ol style="text-align:justify;"><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Search for and use relevant digital and non-digital information from sources other than the module materials.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Compare critically and use different approaches to issues and problems within business management. Engage in critical reflection.</span></li><li><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Consolidate an understanding of academic language and literacy practices in order to effectively engage with the academic knowledge and skills of Level 5 study.&ZeroWidthSpace;&ZeroWidthSpace;</span><br><br></span></li></span></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    B207-B&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Shaping Business Opportunities <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    B207B is an 8-credit (30 points), Level 5 UK-OU based course offered through the Business Program at the Arab Open University as a compulsory course for all students enrolled in all tracks in the program. Entry into this course is contingent upon the successful completion of B207A.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_10">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_10" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Shaping Business Opportunities</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B207-B</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Shaping Business Opportunities</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>B207B is an 8-credit (30 points), Level 5 UK-OU based course offered through the Business Program at the Arab Open University as a compulsory course for all students enrolled in all tracks in the program. Entry into this course is contingent upon the successful completion of B207A.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;This module is designed to provide intermediate conceptual and practical learning to students in management and accounting. The module comprises 16 study weeks (including final assessment).&nbsp;<br><br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong></p><p style="text-align:justify;">At the end of the module, learners will be expected to:</p><ol><li>Develop a critical appreciation of the interactions between various business functions (management and accounting) and the integrative complexity that shapes business innovation.</li><li>Develop knowledge and understanding of the elements required to build long-term success in organizations, and how students can contribute to the fostering of long-term value creation.</li><li><strong>&nbsp;</strong>develop knowledge and critical understanding of the theories, concepts and models of different business functions.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">B. Cognitive skills</span></strong></p><p style="text-align:justify;">At the end of the module learners will be expected to:</p><ol style="text-align:justify;"><li>Select and<strong>&nbsp;</strong>critically analyse information relevant to a particular problem or issue related to business and management.</li><li>Evaluate and compare competing perspectives, theoretical models and concepts in the context of practical situations</li><li>Gather and synthesise material from a variety of sources in constructing arguments applied to business and management&nbsp;&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></p><p>At the end of the module, learners will be expected to:</p><ol><li>&nbsp;Communicate in a professional manner in written work, face to face and online. Plan, monitor and review progress as independent learner, including a focus on personal skills development.</li><li>Develop an awareness of ethical issues and professional standards relevant to business and management&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">D.&nbsp;Key transferable skills&nbsp;</span></strong><br></p><p style="text-align:justify;">At the end of the module, learners will be expected to:</p><ol style="text-align:justify;"><li>Search for and use relevant digital and non-digital information from sources other than the module materials.</li><li>Compare critically and use different approaches to issues and problems within business management. Engage in critical reflection.</li><li><strong>&nbsp;</strong>Consolidate an understanding of academic language and literacy practices in order to effectively engage with the academic knowledge and skills of Level 5 study.&ZeroWidthSpace;&ZeroWidthSpace;<br><br></li></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    BE322/4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Entrepreneurship &amp; Small Business Management <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    BE322 is an introductory four credit undergraduate course. It assumes no deep knowledge of business. Indeed, it provides students with an overview of business in an-increasingly global society. This is not a course of theory; it is more an application or "how-to" course. It is designed to increase awareness of the opportunities and challenges in today's business environment. The success of any business depends upon several factors: marketing, management and leadership, human resources, financing, logistics, planning, and knowledge of the business environment. An overview of business topics will be discussed including the entrepreneur's success factors, developing business plans, forms of business ownership, management and leadership styles, marketing and market research, technology and e-commerce, understanding financial statements and testing the feasibility and viability of a new venture.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_80">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_80" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Entrepreneurship &amp; Small Business Management</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>BE322/4</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Entrepreneurship &amp; Small Business Management</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B120</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>BE322 is an introductory four credit undergraduate course. It assumes no deep knowledge of business. Indeed, it provides students with an overview of business in an-increasingly global society. This is not a course of theory; it is more an application or "how-to" course. It is designed to increase awareness of the opportunities and challenges in today's business environment. The success of any business depends upon several factors: marketing, management and leadership, human resources, financing, logistics, planning, and knowledge of the business environment. An overview of business topics will be discussed including the entrepreneur's success factors, developing business plans, forms of business ownership, management and leadership styles, marketing and market research, technology and e-commerce, understanding financial statements and testing the feasibility and viability of a new venture.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    BUS110&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Introduction to Business <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    "Introduction to Business” is an introductory course, which surveys the role of business in society. At its simplest level, business is the exchange of goods and services for mutual benefit or profit. Students will be exposed to a wide variety of topics including the terms, trends, organizational structure and opportunities inherent in this exchange, the course introduces the student to the contemporary business world, the business of managing, people in organizations, the principles of marketing, managing information, and financial issues.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_7">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_7" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Introduction to Business</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>BUS110</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Introduction to Business</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>"Introduction to Business” is an introductory course, which surveys the role of business in society. At its simplest level, business is the exchange of goods and services for mutual benefit or profit. Students will be exposed to a wide variety of topics including the terms, trends, organizational structure and opportunities inherent in this exchange, the course introduces the student to the contemporary business world, the business of managing, people in organizations, the principles of marketing, managing information, and financial issues.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;The primary objective is to give the student an understanding of basic business principles. Global business, entrepreneurship, management, marketing, information technology, and financial&nbsp;management will be discussed. Another purpose of this course is to build a foundation of knowledge on the different theoretical approaches to management and decision making • develop analytical skills to identify the links between the functional areas in management, organisations, management practices and the business environment&ZeroWidthSpace;.<br></p><p><span class="ms-rteThemeForeColor-2-0" style="text-decoration-style:solid;text-decoration-color:#444444;">Learning Objectives: Upon completion of the course students will have a firm understanding of the following business topics:</span></p><ul><li><span class="ms-rteThemeForeColor-2-0" style="text-decoration-style:solid;text-decoration-color:#444444;">The&nbsp;<span lang="EN-GB" style="font-family:arial, sans-serif;text-decoration-style:solid;text-decoration-color:#444444;">relationship between business and society in a free market economy</span></span></li><li><span class="ms-rteThemeForeColor-2-0" lang="EN-GB" style="font-family:arial, sans-serif;text-decoration-style:solid;text-decoration-color:#444444;">Common forms of business ownership</span></li><li><span class="ms-rteThemeFontFace-1"><span class="ms-rteThemeForeColor-2-0 ms-rteThemeFontFace-1" lang="EN-GB" style="text-decoration-style:solid;text-decoration-color:#444444;">Business ethics and social responsibility</span>&ZeroWidthSpace;<br></span></li><li><span class="ms-rteThemeFontFace-1">International business and the global economy</span></li><li><span class="ms-rteThemeFontFace-1">Fundamentals of business management</span></li><li><span class="ms-rteThemeFontFace-1">Business organization and structure</span></li><li><span class="ms-rteThemeFontFace-1">Human resources, motivation and productivity</span></li><li><span class="ms-rteThemeFontFace-1">Marketing, accounting, finance, operations &ZeroWidthSpace;management and other business specialties</span></li></ul><p><br><br></p><p></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong><br></p><p>At the end of the module, learners will be expected to:</p><ol><li>Identify business functions</li><li>Recognize different business models and forms</li><li>Acquire knowledge of business ethics and social responsibility</li><li>Be aquatinted with the fundamentals of management.&nbsp;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">B. Cognitive skills</span></strong><br></p><p>At the end of the module learners will be expected to:<br></p><ol><li>&nbsp;Differentiate between business structures and business forms.<br></li><li>Examine different models and theories and its effect in business life&nbsp;</li><li>&nbsp;analysing and evaluating different perspectives, identifying biases and hidden assumptions in different models and forms of businesses.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></p><p>At the end of the module, learners will be expected to:<br></p><ol><li>Analyse different business-related situations and forms.<br></li><li>&nbsp;Deduce problems and solutions and its pathways</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">D. Key transferable skills&nbsp;</span></strong><br></p><p>At the end of the module, learners will be expected to:<br></p><ul><li>Read financial and business related reports&ZeroWidthSpace;</li><li>&ZeroWidthSpace;Communicate knowledge and understanding of business issues to different stakeholders.</li><li>Analyse situations in an academic manner.<br><br></li></ul></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    BUS310&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Strategic Management <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Strategic Management: This module examines concepts and  the different approaches to - and techniques of - strategic management including analysis of the external and internal environments, the nature of competitive advantage, development of the organization and how they make strategic choices as to where and how to position themselves in relation to their customers and competitors.
The module   has been designed to encourage and develop greater critical analytical skills especially at level 3. Significant amount of ‘case study’ work have been embedded to develop the students’ analytical and problem solving skills.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_21">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_21" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Strategic Management</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>BUS310</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Strategic Management</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Strategic Management: This module examines concepts and  the different approaches to - and techniques of - strategic management including analysis of the external and internal environments, the nature of competitive advantage, development of the organization and how they make strategic choices as to where and how to position themselves in relation to their customers and competitors.
The module   has been designed to encourage and develop greater critical analytical skills especially at level 3. Significant amount of ‘case study’ work have been embedded to develop the students’ analytical and problem solving skills.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul><li>&ZeroWidthSpace;Provide students with concepts and tangible strategic skills that can readily be put into practice in often&nbsp;&nbsp; changing business environments.&nbsp;</li><li>Present the 21st century competitive/business landscape from a strategic management perspective and to assess how global and technological influences shape it</li><li>Provide students with a critical overview of the main tools of contemporary strategic practice in organizations in a way which is relevant to their professional needs</li><li>Achieving the intended learning outcomes (covering both knowledge and skills) fully supports this aim.</li></ul><p><br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:11pt;line-height:107%;font-family:arial, sans-serif;letter-spacing:-0.3pt;">A</span><span lang="EN-GB" style="font-size:11pt;line-height:107%;font-family:arial, sans-serif;">.<span style="letter-spacing:0.1pt;"> </span><span style="letter-spacing:-0.05pt;">K</span>n<span style="letter-spacing:-0.05pt;">o</span><span style="letter-spacing:0.15pt;">w</span><span style="letter-spacing:0.05pt;">l</span>e<span style="letter-spacing:-0.05pt;">d</span>ge a<span style="letter-spacing:-0.05pt;">n</span>d<span style="letter-spacing:-0.1pt;"> </span>u<span style="letter-spacing:-0.05pt;">n</span><span style="letter-spacing:-0.15pt;">d</span>erstan<span style="letter-spacing:-0.05pt;">d</span><span style="letter-spacing:0.05pt;">i</span>ng</span></strong><br></p><p style="text-align:justify;"><em>A</em><em>t</em><em> </em><em>t</em><em>he</em><em> </em><em>e</em><em>n</em><em>d</em><em> </em><em>of </em><em>t</em><em>he</em><em> </em><em>m</em><em>o</em><em>d</em><em>u</em><em>l</em><em>e</em><em>,</em><em> </em><em>l</em><em>e</em><em>a</em><em>r</em><em>n</em><em>e</em><em>r</em><em>s</em><em> </em><em>w</em><em>il</em><em>l be</em><em> </em><em>ex</em><em>p</em><em>e</em><em>c</em><em>t</em><em>e</em><em>d </em><em>t</em><em>o</em><em>:</em><em> </em><em>de</em><em>v</em><em>e</em><em>l</em><em>o</em><em>p a</em><em>n</em><em>d </em><em>de</em><em>m</em><em>o</em><em>n</em><em>s</em><em>t</em><em>ra</em><em>t</em><em>e </em><em>t</em><em>h</em><em>e </em><em>f</em><em>ol</em><em>l</em><em>o</em><em>w</em><em>i</em><em>n</em><em>g</em><em> </em><em>K</em><em>n</em><em>o</em><em>w</em><em>l</em><em>e</em><em>d</em><em>ge</em><em> </em><em>a</em><em>n</em><em>d </em><em>u</em><em>n</em><em>d</em><em>er</em><em>s</em><em>t</em><em>a</em><em>n</em><em>di</em><em>ng</em><em>:</em></p><ol style="text-align:justify;"><li>The structure and dynamics of business environments; how businesses seek to track and analyse their environments;</li><li>Markets, market economies and how they function; how consumers, firms and governments behave as economic agents; why and how markets fail and how this failure is managed;</li><li>Business processes and how they operate; the nature, structure and functioning of organisations; how and why organisations are changing;</li><li>Key business functions such as Marketing, Human Resources, Information Management, Accounting &amp; Finance, Operations – their nature and contribution to organisational success, their historic origins and their interactions;</li><li>How businesses develop strategies; the different forms and theories of strategy;</li><li>How organisations make decisions and organise decision-making processes; the various sources of decision-making irrationality; the nature, role and implications of governmental, regional and supranational business policy on businesses;<br></li><li>How to apply key ideas in mathematics, including some&nbsp;&nbsp; statistics, and algebra.</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;line-height:107%;font-family:arial, sans-serif;letter-spacing:-0.05pt;">B</span><span lang="EN-GB" style="font-size:11pt;line-height:107%;font-family:arial, sans-serif;">.<span style="letter-spacing:0.1pt;"> </span><span style="letter-spacing:-0.05pt;">C</span>o<span style="letter-spacing:-0.05pt;">g</span>n<span style="letter-spacing:-0.1pt;">i</span><span style="letter-spacing:0.05pt;">ti</span><span style="letter-spacing:-0.15pt;">v</span>e<span style="letter-spacing:0.15pt;"> </span>s<span style="letter-spacing:-0.05pt;">ki</span><span style="letter-spacing:0.05pt;">ll</span>s</span></strong><br></p><p>At the end of the module learners will be expected to:</p><ol><li>&nbsp;Read material questioningly, identifying and recording key ideas and concepts in business studies;<br></li><li>&nbsp;Synthesise material from a variety of sources, analysing and evaluating different perspectives, identifying biases and hidden assumptions;<br></li><li>Classify, recognise and organise material in distinct and relevant categories;<br></li><li>&nbsp;Construct, defend and evaluate an argument, using relevant evidence, giving reasons for conclusions.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;line-height:107%;font-family:arial, sans-serif;letter-spacing:-0.05pt;">C</span><span lang="EN-GB" style="font-size:11pt;line-height:107%;font-family:arial, sans-serif;">.<span style="letter-spacing:0.1pt;"> </span><span style="letter-spacing:-0.05pt;">P</span>ra<span style="letter-spacing:-0.15pt;">c</span><span style="letter-spacing:0.05pt;">ti</span>c<span style="letter-spacing:-0.15pt;">a</span>l<span style="letter-spacing:0.1pt;"> </span>a<span style="letter-spacing:-0.05pt;">n</span>d
pr<span style="letter-spacing:-0.15pt;">o</span><span style="letter-spacing:0.05pt;">f</span>e<span style="letter-spacing:-0.15pt;">s</span>sion<span style="letter-spacing:-0.05pt;">a</span>l
s<span style="letter-spacing:-0.05pt;">ki</span><span style="letter-spacing:0.05pt;">ll</span>s</span></strong><br></p><p>At the end of the module, learners will be expected to:</p><ol><li>Transfer and use relevant key skills in the workplace context;</li><li>Use the more specific knowledge, analytic skills and methods, rooted in the different disciplines as a strong basis for work in many professions;&nbsp;Students will have become better informed, more active and questioning members of an organisation by:</li><li>The ability to engage critically with the underlying challenges and problems facing a business;</li><li>&nbsp;The ability to identify and evaluate conflicting arguments, including recognising the significance of different value positions in these arguments.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;line-height:107%;font-family:arial, sans-serif;"><strong><span lang="EN-GB" style="font-size:11pt;line-height:107%;font-family:arial, sans-serif;">D. <span style="letter-spacing:-0.05pt;">K</span><span style="letter-spacing:0.1pt;">e</span>y<span style="letter-spacing:-0.2pt;"> </span><span style="letter-spacing:0.05pt;">t</span>ran<span style="letter-spacing:-0.05pt;">s</span><span style="letter-spacing:0.05pt;">f</span>era<span style="letter-spacing:-0.15pt;">b</span><span style="letter-spacing:0.05pt;">l</span>e s<span style="letter-spacing:-0.1pt;">k</span><span style="letter-spacing:-0.05pt;">i</span><span style="letter-spacing:0.05pt;">l</span><span style="letter-spacing:-0.05pt;">l</span>s</span></strong><br></span></strong></p><p style="text-align:justify;">At the end of the module, learners will be expected to:&ZeroWidthSpace;</p><ol style="text-align:justify;"><li>Interpersonal skills of effective listening, negotiating, persuasion and presentation;</li><li>Ability to conduct research into business and management issues, either individually or as part of a team for projects/dissertations/presentations. This requires familiarity with and an evaluative approach to a range of business data, sources of information and appropriate methodologies, and for such to inform the overall learning process; including the development of personal and team attributes and capabilities for entrepreneurial success;</li><li>Self reflection and criticality including self awareness, openness and sensitivity to diversity in terms of people, cultures, business and management issues;</li><li>Skills of learning to learn and developing a continuing appetite for learning; reflective, adaptive and collaborative learning.</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;line-height:107%;font-family:arial, sans-serif;"><br></span></strong></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    CH101&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Chinese for Beginners (I) <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The course introduces the student to the basics of Chinese (Mandarin). These include the alphabet, common everyday expressions, simple sentences, short dialogues and small paragraphs. The four skills of reading, writing, listening and speaking will be equally emphasized. However, as we live in the age of the image, students will have ample exposure to a variety of audio-visual material which boost their command of the language at the beginner’s level.  The communicative approach is to be adopted in face-to-face tutorials and the various methods of enabling students to learn on their own will be prioritized.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_81">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_81" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Chinese for Beginners (I)</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>CH101</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Chinese for Beginners (I)</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>The course introduces the student to the basics of Chinese (Mandarin). These include the alphabet, common everyday expressions, simple sentences, short dialogues and small paragraphs. The four skills of reading, writing, listening and speaking will be equally emphasized. However, as we live in the age of the image, students will have ample exposure to a variety of audio-visual material which boost their command of the language at the beginner’s level.  The communicative approach is to be adopted in face-to-face tutorials and the various methods of enabling students to learn on their own will be prioritized.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    CH102&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Chinese for Beginners (II) <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The course builds on what the student has learnt in level (1). Toward this end, it introduces the student to more everyday expressions, more widely-used short sentences, some compound and complex sentences, medium-size dialogues, and short passages. While the skills of listening and speaking will be receiving adequate attention, more emphasis is to be placed on the skills of reading and writing.  Face-to-face tutorials will be communicative and students will be empowered to learn on their own.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_82">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_82" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Chinese for Beginners (II)</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>CH102</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Chinese for Beginners (II)</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>CH101</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>The course builds on what the student has learnt in level (1). Toward this end, it introduces the student to more everyday expressions, more widely-used short sentences, some compound and complex sentences, medium-size dialogues, and short passages. While the skills of listening and speaking will be receiving adequate attention, more emphasis is to be placed on the skills of reading and writing.  Face-to-face tutorials will be communicative and students will be empowered to learn on their own.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    CS240&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Introduction to computer Graphics <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module targets to cope with the current advances in computer graphics and multimedia and providing clear and concise explanations of the basic concepts of computer graphics and multimedia. This module is expected to enable students to gain understanding of basics of modelling, viewing, animation principles in both 2D and 3D and the impact of such topics on modern multimedia aspects.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_98">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_98" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Introduction to computer Graphics</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>CS240</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Introduction to computer Graphics</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>M132</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module targets to cope with the current advances in computer graphics and multimedia and providing clear and concise explanations of the basic concepts of computer graphics and multimedia. This module is expected to enable students to gain understanding of basics of modelling, viewing, animation principles in both 2D and 3D and the impact of such topics on modern multimedia aspects.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p></p><ul><li>&ZeroWidthSpace;Introduce all aspects of the hardware and software components of computer graphics.</li><li>Provide Knowledge to perform 2D and 3D geometric transformations.</li><li>&nbsp;Describe the algorithms for projection, viewing and clipping of graphs.</li><li>Identify how to graphics software and hardware.</li><li>&nbsp;Provide Knowledge to evaluate the performance of graphics systems.&ZeroWidthSpace;<br><br></li></ul><p>&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;</p><table class="ms-formtable" border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-top:8px;"><tbody><tr><td valign="top" class="ms-formbody" width="350px"><div aria-labelledby="ctl00_ctl39_g_eb7daa64_36cc_4108_a9f5_cc8a9db927e9_ctl00_ctl05_ctl09_ctl00_ctl00_ctl05_ctl00_label" style="display:inline;"><p></p><p><span class="ms-rteThemeFontFace-1"><br class="Apple-interchange-newline">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1">Upon completing this module,&nbsp;<span lang="EN-GB"><strong>student should be able to:</strong></span></span></p><ol><li><span class="ms-rteThemeFontFace-1">Describe the basic principles of computer graphics.</span></li><li><span class="ms-rteThemeFontFace-1">Explain the different operations in graphics systems such as transformations, projects, views, texturing, lighting, shading, animation and clipping.</span></li><li><span class="ms-rteThemeFontFace-1">Select the suitable hardware and software of a graphics system for a specific application.</span></li><li><span class="ms-rteThemeFontFace-1">Explain graphics algorithms.</span></li><li><span class="ms-rteThemeFontFace-1">Develop graphics applications in Java.</span></li></ol><p><span class="ms-rteThemeFontFace-1"><strong>B. Cognitive skills</strong><br></span></p><p><span class="ms-rteThemeFontFace-1">Upon completing this module,&nbsp;<span lang="EN-GB"><strong>student should be able to:</strong></span></span></p><ol><li><span class="ms-rteThemeFontFace-1">Evaluate graphics hardware and software.</span></li><li><span class="ms-rteThemeFontFace-1">Compare the different computer graphics applications.</span></li><li><span class="ms-rteThemeFontFace-1">Select the suitable graphics hardware for different applications.</span></li><li><span class="ms-rteThemeFontFace-1">Evaluate 3D modelling techniques.</span></li></ol><p><span class="ms-rteThemeFontFace-1"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1">Upon completing this module,&nbsp;<span lang="EN-GB"><strong>student should be able to:</strong></span></span></p><ol><li><span class="ms-rteThemeFontFace-1">Develop graphics applications using advanced APIs</span></li><li><span class="ms-rteThemeFontFace-1">Apply computer graphics concepts and techniques to develop graphics and visualization applications</span></li><li><span class="ms-rteThemeFontFace-1">Model 3D objects.<br></span></li></ol><p><span class="ms-rteThemeFontFace-1"><strong><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1">Upon completing this module,&nbsp;<span lang="EN-GB"><strong>student should be able to:</strong></span></span></p><ol><li><span class="ms-rteThemeFontFace-1">Effectively communicate oral and written.</span></li><li><span class="ms-rteThemeFontFace-1">Work in a team.</span></li><li><span class="ms-rteThemeFontFace-1">&ZeroWidthSpace;Effectively manage resources and time.</span></li></ol><p>&ZeroWidthSpace;<br><br></p></div></td></tr></tbody></table><p><br></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    EL111&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Communication Skills in English 1 <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    EL111 is three credit hour university requirements. It aims to develop in students the skills of listening, speaking, reading and writing in English, together with attention to function and correct use of vocabulary and grammar. The course introduces thematic topics which aim at developing critical thinking skills. In addition, learning strategies such as prior knowledge, scanning for specific information, skimming for main idea and getting meaning from context are emphasized.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_77">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_77" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Communication Skills in English 1</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>EL111</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Communication Skills in English 1</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>EF003</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>EL111 is three credit hour university requirements. It aims to develop in students the skills of listening, speaking, reading and writing in English, together with attention to function and correct use of vocabulary and grammar. The course introduces thematic topics which aim at developing critical thinking skills. In addition, learning strategies such as prior knowledge, scanning for specific information, skimming for main idea and getting meaning from context are emphasized.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    EL112&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Communication Skills in English 2 <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    EL112 is an advanced integrated skills course which builds on knowledge gained from EL111. The course continues to develop the four communication skills of listening, speaking, reading and writing to a more advanced level. In addition, students start to write longer essays.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_78">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_78" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Communication Skills in English 2</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>EL112</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Communication Skills in English 2</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>EL111</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>EL112 is an advanced integrated skills course which builds on knowledge gained from EL111. The course continues to develop the four communication skills of listening, speaking, reading and writing to a more advanced level. In addition, students start to write longer essays.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    EL118&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reading Comprehension <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    	
This is a four-credit-hour module of one semester in length. The module aims to help students become better readers of English texts and build their vocabulary. It focuses on expanding students’ reading skills and vocabulary use so that they can cope with different academic, professional and social situations effectively. The course applies the Interactive Reading model where reading is an active process in which readers draw upon top-down processing (bringing meaning to the text), as well as bottom-up processing (decoding words and other details of language). The top-down aspect of this construct suggests that reading is facilitated by interesting and relevant reading materials that activate a range of knowledge in a reader's mind. This knowledge is refined and extended during the act of reading. The bottom-up aspect of this model suggests that the students need to pay attention to language proficiency, including vocabulary. As an academic reading course, it addresses the teaching of higher level reading strategies without neglecting the need for language support. In addition, it addresses both sides of the interactive model. High-interest academic readings and activities provide students with opportunities to draw upon authentic life experience in their mastery of a wide variety of reading strategies and skills, including
• previewing
• outlining
• skimming and scanning
• using context clues to clarify meaning
• finding the main idea
• isolating causes and effects
• annotating and highlighting
• categorizing
• interpreting visuals
• describing trends
• making inferences.
• understanding analogies
• analysing criteria
• analysing advantages and disadvantages
• identifying ethics and values
• synthesizing information from several sources
• summarizing
• evaluating generalizations
The course optimizes the reciprocal relationship between reading and vocabulary. Rich vocabulary instruction and practice that targets vocabulary from the Academic Word List (AWL) provide opportunities for students to improve their language proficiency and their ability to decode and process vocabulary. The course also provides some resources to help students read with comprehension and use that knowledge to develop both a rich academic vocabulary and overall academic language proficiency, especially reading skills. The module prepares the students to write academic essays reflecting on a topic under discussion that will help them pursue their academic study throughout different core modules.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_83">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_83" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Reading Comprehension</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>EL118</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Reading Comprehension</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>EL111</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>	
This is a four-credit-hour module of one semester in length. The module aims to help students become better readers of English texts and build their vocabulary. It focuses on expanding students’ reading skills and vocabulary use so that they can cope with different academic, professional and social situations effectively. The course applies the Interactive Reading model where reading is an active process in which readers draw upon top-down processing (bringing meaning to the text), as well as bottom-up processing (decoding words and other details of language). The top-down aspect of this construct suggests that reading is facilitated by interesting and relevant reading materials that activate a range of knowledge in a reader's mind. This knowledge is refined and extended during the act of reading. The bottom-up aspect of this model suggests that the students need to pay attention to language proficiency, including vocabulary. As an academic reading course, it addresses the teaching of higher level reading strategies without neglecting the need for language support. In addition, it addresses both sides of the interactive model. High-interest academic readings and activities provide students with opportunities to draw upon authentic life experience in their mastery of a wide variety of reading strategies and skills, including
• previewing
• outlining
• skimming and scanning
• using context clues to clarify meaning
• finding the main idea
• isolating causes and effects
• annotating and highlighting
• categorizing
• interpreting visuals
• describing trends
• making inferences.
• understanding analogies
• analysing criteria
• analysing advantages and disadvantages
• identifying ethics and values
• synthesizing information from several sources
• summarizing
• evaluating generalizations
The course optimizes the reciprocal relationship between reading and vocabulary. Rich vocabulary instruction and practice that targets vocabulary from the Academic Word List (AWL) provide opportunities for students to improve their language proficiency and their ability to decode and process vocabulary. The course also provides some resources to help students read with comprehension and use that knowledge to develop both a rich academic vocabulary and overall academic language proficiency, especially reading skills. The module prepares the students to write academic essays reflecting on a topic under discussion that will help them pursue their academic study throughout different core modules.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p></p><div><table class="ms-formtable" border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-top:8px;"><tbody><tr><td valign="top" class="ms-formbody" width="350px"><div aria-labelledby="ctl00_ctl39_g_44a2afab_1d6b_4771_bcfb_6d17c6b0e096_ctl00_ctl05_ctl07_ctl00_ctl00_ctl05_ctl00_label" style="display:inline;"><p>&ZeroWidthSpace;</p><p style="text-align:justify;"><em>The module aims to provide the learners with necessary skills trough:</em></p><p style="text-align:justify;">&nbsp;</p><p style="text-align:justify;">1. Providing the students with opportunities to draw upon life experience in their mastery of a wide variety of reading strategies and skills that include previewing, scanning, using contextual clues to get the meaning, finding the main idea, summarizing and making inferences.</p><p style="text-align:justify;">2. Improving the students' language proficiency and the students' ability to decode and process meaning.</p><p style="text-align:justify;">3. Helping the students become independent learners by taking the responsibility of building their own vocabulary repertoire</p><p style="text-align:justify;">4. Guiding the students to notice and effectively practice new vocabulary items as they encounter them.</p><p>5. Enhancing students' academic proficiency by highlighting the reciprocal relationship between reading comprehension and reflection writing.&ZeroWidthSpace;<br><br></p></div></td></tr></tbody></table></div><p>&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;</p><p style="text-align:justify;"><strong>A.</strong>&nbsp;&nbsp;&nbsp;<strong>Knowledge and understanding</strong></p><p style="text-align:justify;"><em>At the end of the module, learners will be expected to:</em></p><p style="text-align:justify;"><strong>A1.</strong>&nbsp;demonstrate understanding of any given reading passages by responding correctly to its tasks and activities individually or in groups.</p><p style="text-align:justify;"><strong>A2.</strong>&nbsp;show knowledge and understanding of the learned reading strategies.</p><p style="text-align:justify;"><strong>A3.</strong>&nbsp;show recognition of the various “meanings" of words to reach a better understanding of the context and the written word.</p><p style="text-align:justify;"><strong>A4.</strong>&nbsp;reveal awareness of appropriate language structures and vocabulary items suitable for different contexts and situations.</p><p style="text-align:justify;">&nbsp;</p><p><strong>B.</strong>&nbsp;&nbsp;&nbsp;<strong>Cognitive skills</strong><br><br><em>At the end of the module, learners will be expected to:</em><br><br><strong>B1.</strong>&nbsp;search for and collect specific data related to the topics under discussion.</p><p style="text-align:justify;"><strong>B2.</strong>&nbsp;draw conclusions for the discussed topics based on the collected data and analyzed information.</p><p style="text-align:justify;"><strong>B3.</strong>&nbsp;incorporate in writing the words learned in real life scenarios.</p><p style="text-align:justify;"><strong>B4</strong>. improve the analytical and critical thinking skills through the identification of possible “meanings".</p><p><strong>B5.</strong>&nbsp;analyze language functions used and identify useful language expressions.</p><p>&nbsp;</p><p><strong>C.</strong>&nbsp;&nbsp;&nbsp;<strong>Practical and professional skills</strong><br><br><em>At the end of the module, learners will be expected to:</em></p><p style="text-align:justify;"><strong>C1.</strong>&nbsp;communicate in English orally and in writing on diverse occasions.</p><p style="text-align:justify;">&nbsp;</p><p style="text-align:justify;"><strong>C2.</strong>&nbsp;identify problems in the given topics and provide creative solutions.</p><p style="text-align:justify;">&nbsp;</p><p style="text-align:justify;"><strong>C3.</strong>&nbsp;give oral presentations using power points, flipcharts, pictures, role plays, etc. to discuss what has been read orally.</p><p style="text-align:justify;">&nbsp;</p><p><strong>C4.</strong>&nbsp;assess the work done using self/peer-assessment.</p><p>&nbsp;</p><p><strong>D.</strong>&nbsp;&nbsp;&nbsp;<strong>&nbsp;</strong><strong>Key transferable skills</strong><br><br><strong>&nbsp;</strong></p><p style="text-align:justify;"><em>At the end of the module, learners will be expected to:</em><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></p><p style="text-align:justify;"><strong>D1.</strong>&nbsp;enrich vocabulary repertoire through exploring new assigned topics and writing on those topics</p><p style="text-align:justify;"><strong>D2.</strong>&nbsp;develop communicative confidence (as reader and writer)</p><p style="text-align:justify;"><strong>D3.</strong>&nbsp;discuss all posed topics, problems, provided solutions and drawn conclusions.</p><p><strong>D4.</strong>&nbsp;develop effective presentation skills that would enhance self-confidence.&ZeroWidthSpace;&ZeroWidthSpace;<br><br></p><p><br></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    FR101&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;French for Beginners (I) <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The course introduces the student to the basics of French. These include the alphabet, common everyday expressions, simple sentences, short dialogues and small paragraphs. The four skills of reading, writing, listening and speaking will be equally emphasized. However, as we live in the age of the image, students will have ample exposure to a variety of audio-visual material which boost their command of the language at the beginner’s level.  The communicative approach is to be adopted in face-to-face tutorials and the various methods of enabling students to learn on their own will be prioritized.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_84">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_84" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">French for Beginners (I)</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>FR101</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>French for Beginners (I)</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>The course introduces the student to the basics of French. These include the alphabet, common everyday expressions, simple sentences, short dialogues and small paragraphs. The four skills of reading, writing, listening and speaking will be equally emphasized. However, as we live in the age of the image, students will have ample exposure to a variety of audio-visual material which boost their command of the language at the beginner’s level.  The communicative approach is to be adopted in face-to-face tutorials and the various methods of enabling students to learn on their own will be prioritized.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    FR102&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;French for Beginners (II) <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The course builds on what the student has learnt in level (1). Toward this end, it introduces the student to more everyday expressions, more widely-used short sentences, some compound and complex sentences, medium-size dialogues, and short passages. While the skills of listening and speaking will be receiving adequate attention, more emphasis is to be placed on the skills of reading and writing.  Face-to-face tutorials will be communicative and students will be empowered to learn on their own.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_85">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_85" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">French for Beginners (II)</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>FR102</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>French for Beginners (II)</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>FR101</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>The course builds on what the student has learnt in level (1). Toward this end, it introduces the student to more everyday expressions, more widely-used short sentences, some compound and complex sentences, medium-size dialogues, and short passages. While the skills of listening and speaking will be receiving adequate attention, more emphasis is to be placed on the skills of reading and writing.  Face-to-face tutorials will be communicative and students will be empowered to learn on their own.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    GR 117&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Empowerment of Women <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This course focuses on empowering women and activating their role in leading political, economic and social development.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_102">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_102" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Empowerment of Women</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>GR 117</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Empowerment of Women</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This course focuses on empowering women and activating their role in leading political, economic and social development.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p></p><p>&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    GR101&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Self-Learning Skills <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    GR101 focuses on developing self-learning skills. It prepares students for university studying and specifically time management, good study habits, critical and analytic thinking styles.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_79">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_79" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Self-Learning Skills</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>GR101</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Self-Learning Skills</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>GR101 focuses on developing self-learning skills. It prepares students for university studying and specifically time management, good study habits, critical and analytic thinking styles.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    GR111&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Arabic Islamic Civilization <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Overall views in the history of Arabic-Islamic Civilization.
Concepts and Social Issues.
The effect of Islamic Civilization on the European Renaissance.
Trends of Stagnation in the Islamic Civilization.
Modern Arabic Renaissance.
Islamic Arts and Architecture.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_86">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_86" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Arabic Islamic Civilization</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>GR111</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Arabic Islamic Civilization</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Overall views in the history of Arabic-Islamic Civilization.
Concepts and Social Issues.
The effect of Islamic Civilization on the European Renaissance.
Trends of Stagnation in the Islamic Civilization.
Modern Arabic Renaissance.
Islamic Arts and Architecture.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    GR112&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Issues and Problems of Development in the Arab Region <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    GR112 deals with issues and problems related to the development of the Arab region, specifically human development and its social indicators, Arab culture, education, mass media, health, nutrition, women, environment and natural resources.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_87">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_87" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Issues and Problems of Development in the Arab Region</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>GR112</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Issues and Problems of Development in the Arab Region</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>GR112 deals with issues and problems related to the development of the Arab region, specifically human development and its social indicators, Arab culture, education, mass media, health, nutrition, women, environment and natural resources.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    GR116&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Empowerment of Youth <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This course aims to empower and prepare the youth to engage in political, social and economic life, raising awareness in these aspects and developing their leadership skills.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_101">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_101" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Empowerment of Youth</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>GR116</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Empowerment of Youth</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This course aims to empower and prepare the youth to engage in political, social and economic life, raising awareness in these aspects and developing their leadership skills.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    GR118&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Life skills and Coexistence <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This course enables individuals to develop their positive and adaptive behaviors to effectively deal with the requirements and challenges of life. It aims at helping students to acquire skills such as: effective communication, problem solving, stress management and leadership. It also deals with issues such as: human and women rights, democracy, accepting others and tolerance.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_103">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_103" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Life skills and Coexistence</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>GR118</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Life skills and Coexistence</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This course enables individuals to develop their positive and adaptive behaviors to effectively deal with the requirements and challenges of life. It aims at helping students to acquire skills such as: effective communication, problem solving, stress management and leadership. It also deals with issues such as: human and women rights, democracy, accepting others and tolerance.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    GR121&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Environment and Health <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The course focuses on introduction social and natural sciences which study the relationship between human activity and human environment. Looking at various topics using a case-study approach.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_104">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_104" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Environment and Health</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>GR121</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Environment and Health</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>The course focuses on introduction social and natural sciences which study the relationship between human activity and human environment. Looking at various topics using a case-study approach.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    GR131&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;History and civilization of the Sultanate of Oman <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    GR131 introduces students to current issues of interest to socio-economic development at the local and regional levels.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_90">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_90" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">History and civilization of the Sultanate of Oman</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>GR131</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>History and civilization of the Sultanate of Oman</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>GR131 introduces students to current issues of interest to socio-economic development at the local and regional levels.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    M105&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Introduction to Programming Using Java <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module is an introductory level programming module and it is meant to provide basic foundation in computer programming to students. Students will learn how to develop solutions (algorithms) using pseudocode to solve simple problems. Thereafter, they will learn how to implement these solutions using a programming language (Java). This module serves as foundation for second level programming modules.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_100">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_100" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Introduction to Programming Using Java</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>M105</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Introduction to Programming Using Java</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>EL111</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module is an introductory level programming module and it is meant to provide basic foundation in computer programming to students. Students will learn how to develop solutions (algorithms) using pseudocode to solve simple problems. Thereafter, they will learn how to implement these solutions using a programming language (Java). This module serves as foundation for second level programming modules.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;</p><div><table class="ms-formtable" border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-top:8px;"><tbody><tr><td valign="top" class="ms-formbody" width="350px"><div aria-labelledby="ctl00_ctl39_g_eb7daa64_36cc_4108_a9f5_cc8a9db927e9_ctl00_ctl05_ctl07_ctl00_ctl00_ctl05_ctl00_label" style="display:inline;"><p>&ZeroWidthSpace;<strong>The module aims to:</strong></p><ul><li>Introduce the technique of solving simple problems using pseudocode.</li><li>Introduce Java programming via writing, compiling and executing simple programs.</li><li>Present how to store and deal with data including variables, constants, and expressions.</li><li>Cover deeply the concepts of program control structure and illustrate each concept with a diagrammatic notation using UML.</li><li>Present how these concepts are implemented in Java.</li><li>Introduce the concept of modularization and how to write Java methods.</li><li>Present how to deal with basic data structures like strings, arrays and two dimensional arrays.<br><br></li></ul></div></td></tr></tbody></table></div><p>&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;</p><div><table class="ms-formtable" border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-top:8px;"><tbody><tr><td valign="top" class="ms-formbody" width="350px"><div aria-labelledby="ctl00_ctl39_g_eb7daa64_36cc_4108_a9f5_cc8a9db927e9_ctl00_ctl05_ctl09_ctl00_ctl00_ctl05_ctl00_label" style="display:inline;"><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">A. Knowledge and understanding</span></strong><br></p><p><strong>After studying the module,&nbsp;</strong><strong>the student will be able to</strong><strong>:</strong></p><ol><li>Understanding of the design and programming processes</li><li>Knowledge of the main constructs and mechanisms in programming using Java language.</li><li>Understanding of the techniques used in developing a medium Java application.</li><li>Understanding of the basic data structures like strings, arrays and two dimensional arrays.</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;">B. Cognitive skills</span></strong><br></p><p><strong>After studying the module,&nbsp;</strong><strong>the student should be able to</strong><strong>:</strong></p><ol><li>Describe and apply key concepts and techniques in software design and development.</li><li>Analyse and abstract away from the details of a problem.</li><li>Design and formulate an appropriate solution to a problem and evaluate it.</li><li>Deal professionally with the basic data structures.</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;">C. Practical and professional skills</span></strong><br></p><p><strong>After studying the module,&nbsp;</strong><strong>the student should be able to</strong><strong>:</strong></p><ol><li>Create, develop and trace Java programs.</li><li>Use software tools such&nbsp;as a Java IDE and an On-line Java compiler.</li><li>Use appropriate programming skills.</li><li>Traverse data in the basic data structures in a professional way.&nbsp;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;">D. Key transferable skills&nbsp;</span></strong><br></p><p><strong>After studying the module,&nbsp;</strong><strong>the student should be able to</strong><strong>:</strong></p><ol><li>Find information from a range of sources to support a task.</li><li>Plan medium tasks.</li><li>Use Java libraries.</li><li>Use appropriate numerical, mathematical and abstraction skills.&nbsp;&ZeroWidthSpace;<br><br></li></ol></div></td></tr></tbody></table></div><p><br></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    M109 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; .NET Programming <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module is intended to introduce and present the fundamental skills that are required to design and develop object-oriented programs and applications in .NET Framework
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_37">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_37" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title"> .NET Programming</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>M109 </td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td> .NET Programming</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module is intended to introduce and present the fundamental skills that are required to design and develop object-oriented programs and applications in .NET Framework</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul><li>To understand the .NET framework architecture.</li><li>To provide students with a range of skills to analyze a problem and construct a .NET program that solves it.</li><li>To provide the principles of object oriented programming. </li><li>To implement object-oriented concepts in .NET environment.</li><li>To understand the Visual Studio Integrated Development Environment</li><li>To develop .NET applications using the selected programming language.</li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<span class="ms-rteThemeFontFace-1" lang="EN-GB" style="font-size:13px;"><span lang="EN-GB" style="line-height:107%;letter-spacing:-0.3pt;"><strong>A</strong></span><span lang="EN-GB" style="line-height:107%;"><strong>.</strong><span style="letter-spacing:0.1pt;"> </span><span style="letter-spacing:-0.05pt;"><strong>K</strong></span><strong>n</strong><span style="letter-spacing:-0.05pt;"><strong>o</strong></span><span style="letter-spacing:0.15pt;"><strong>w</strong></span><span style="letter-spacing:0.05pt;"><strong>l</strong></span><strong>e</strong><span style="letter-spacing:-0.05pt;"><strong>d</strong></span><strong>ge a</strong><span style="letter-spacing:-0.05pt;"><strong>n</strong></span><strong>d</strong><span style="letter-spacing:-0.1pt;"> </span><strong>u</strong><span style="letter-spacing:-0.05pt;"><strong>n</strong></span><span style="letter-spacing:-0.15pt;"><strong>d</strong></span><strong>erstan</strong><span style="letter-spacing:-0.05pt;"><strong>d</strong></span><span style="letter-spacing:0.05pt;"><strong>i</strong></span><strong>ng</strong></span><br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Explain .NET Platform.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Describe data types, variables, constants, operators and built-in functions in the selected .NET programming language.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Discuss decision-making and looping statements.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Explain object oriented concepts such as classes, objects and methods.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Describe the features of object oriented programming such as Inheritance and Polymorphism.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Explain the concept of arrays.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Identify errors and different types of exceptions in a .NET program. </span></li></span></ol><div><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>B. Cognitive skills</strong><br></span></div><div><br class="ms-rteThemeFontFace-1"></div><div><span style="font-size:13px;"><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this module, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Develop appropriate programs in .NET framework.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Apply object oriented concepts in .NET framework.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Test and debug a .NET program</span></li></span></ol><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>C. Practical and professional skills</strong></span><br class="ms-rteThemeFontFace-1"></span></div><div><br class="ms-rteThemeFontFace-1"></div><div><span style="font-size:13px;"><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this module, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Develop programming skills in .NET platform.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use variables, constants, operators, built-in functions, methods and arrays in a .NET program.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Write codes in a .NET programming language that make use of structured programming constructs of sequence, selection and repetition. </span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Apply classes, objects and other object oriented concepts such as inheritance and polymorphism in a .NET program.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Test and debug .NET programs.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use the Visual Studio IDE to build .NET applications using the selected .NET programming language.</span></li></span></ol></span></div><div><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>D. Key transferable skills </strong><br></span></div><div><br class="ms-rteThemeFontFace-1"></div><div><span style="font-size:13px;"><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this module, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Collaborate effectively within a group using electronic conferencing techniques.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Facilitate discussions in a conference.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Develop self- learning and performance.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Discuss about testing strategies, design, and code.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use electronic media (the web and electronic conferencing) for information retrieval and communication.</span></li></span></ol><br></span></div></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    M131&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Discrete Mathematics <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    	
This is an elementary level module which introduces various topics in discrete mathematics. It offers a clear and comprehensive survey of logic operations, predicates, quantifiers, sets, functions, relations. Also, the module provides the concept of permutations, combinations and counting techniques which are needed as prerequisite in most of technology and communication modules. Moreover, the module gives some knowledge of relevant algorithmic ideas in number theory and cryptography that are widely used in data structure, data base, programming, data communication and in scientific research.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_95">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_95" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Discrete Mathematics</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>M131</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Discrete Mathematics</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>EL111</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>	
This is an elementary level module which introduces various topics in discrete mathematics. It offers a clear and comprehensive survey of logic operations, predicates, quantifiers, sets, functions, relations. Also, the module provides the concept of permutations, combinations and counting techniques which are needed as prerequisite in most of technology and communication modules. Moreover, the module gives some knowledge of relevant algorithmic ideas in number theory and cryptography that are widely used in data structure, data base, programming, data communication and in scientific research.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p></p><div><table class="ms-formtable" border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-top:8px;"><tbody><tr><td valign="top" class="ms-formbody" width="350px"><div aria-labelledby="ctl00_ctl39_g_eb7daa64_36cc_4108_a9f5_cc8a9db927e9_ctl00_ctl05_ctl07_ctl00_ctl00_ctl05_ctl00_label" style="display:inline;"><p>&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;The course aims to:<br></p><ul><li>Introduce basic notations used in&nbsp; discrete Mathematics associated with information and communication technology</li><li>Teach the rudiments of elementary mathematical reasoning.</li><li>Prepare students for the theoretical parts of further courses in information technology.</li><li>Explain logic from a mathematical perspective and relating it to computer applications.</li><li>Introduce set theory, relations, functions, graphs, equivalence relations, and partial orderings.</li><li>Provide concepts of permutation, combination and any other counting techniques.&ZeroWidthSpace;<br><br><br></li></ul></div></td></tr></tbody></table></div><p>&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;</p><div><table class="ms-formtable" border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-top:8px;"><tbody><tr><td valign="top" class="ms-formbody" width="350px"><div aria-labelledby="ctl00_ctl39_g_eb7daa64_36cc_4108_a9f5_cc8a9db927e9_ctl00_ctl05_ctl09_ctl00_ctl00_ctl05_ctl00_label" style="display:inline;"><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong><br></p><p>Students will be able to:</p><ol><li>Identify propositional logic, logical equivalence, predicates and quantifiers.</li><li>Describe the Integers and division functions, prime number and prime factorization, least common multiple and highest common factors.</li><li>Define sets, functions and binary relations, their properties and representations. Know the major types of binary relations on a set, equivalence relations and partial orderings.</li><li>Use matrices to represent relations, graphs and trees.</li><li>Recognize basic properties of counting techniques using permutation and combination properties.&nbsp;&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">B. Cognitive skills</span></strong><br></p><p>Students will be able to:</p><ol><li>Deal with mathematical and logical arguments and carry out mathematical and logical manipulations.</li><li>Acquire a good understanding of the concepts and methods of discrete mathematics described in detail in the syllabus.</li><li>Be familiar with mathematical notations related to computer science.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></p><p>Students will be able to:</p><ol><li>Prove any simple mathematical theory using logic laws</li><li>Use any or all of the previous tools in a significant information and communication technology application such as cryptography.</li><li>Apply combinatorial principles and discrete mathematical structures that are central to mathematics and information technology.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">D. Key transferable skills</span></strong><br></p><p>Students will be able to:</p><ol><li>Demonstrate study skills at a level appropriate to higher education, such as timetabling study; read critically for meaning and take effective notes; and use study aids such as dictionaries and glossaries;</li><li>Present &nbsp;and communicate basic mathematical and logical arguments; communicate appropriately with their tutor and other students using email and online conferences;</li><li>Locate information on a given subject from the World Wide Web&ZeroWidthSpace;&ZeroWidthSpace;<br><br></li></ol></div></td></tr></tbody></table></div><p><br></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    M132&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Linear Algebra <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    	
The course introduces a range of ideas concerning matrices and its applications, matrix operations that are widely used in data structure, programming, data communication, digital signal processing and in scientific research. The course shows algorithmic method to solve systems of linear equations. Moreover, it includes concept of vector spaces and subspace that are used to construct algebraic codes. Also, it introduces the meaning of basis and dimension of a subspace the vector space Rn. The concept of linear transformation between two vector spaces together with null space and rank are also included. Finally, the course introduce the idea of characteristic values/vectors and diagonalization.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_94">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_94" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Linear Algebra</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>M132</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Linear Algebra</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>	
The course introduces a range of ideas concerning matrices and its applications, matrix operations that are widely used in data structure, programming, data communication, digital signal processing and in scientific research. The course shows algorithmic method to solve systems of linear equations. Moreover, it includes concept of vector spaces and subspace that are used to construct algebraic codes. Also, it introduces the meaning of basis and dimension of a subspace the vector space Rn. The concept of linear transformation between two vector spaces together with null space and rank are also included. Finally, the course introduce the idea of characteristic values/vectors and diagonalization.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;</p><ul><li>Extend the students' basic mathematical awareness and skills in matrices and matrix operations.</li><li>Give the study skills necessary for students to be able to solve system of linear equations.</li><li>Provide a range of useful ideas such as linear combinations and linear independence.</li><li>Present some important mathematical terms such as span, basis and dimensions.</li><li>Upgrade the concept of linear transformation necessary for other compulsory technology and communication modules.</li><li>Give a feeling for the mathematical approach to the study of computer science.&nbsp;<br><br></li></ul><p>&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;</p><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong><br></p><p>Student will be able to:</p><ol><li>Define and classify type of matrices and perform matrix operations.</li><li>Solve problems in information systems and communication using matrix techniques.</li><li>Use and apply linear algebra knowledge and concepts to information technologies and computing.</li><li>Be familiar with different terminologies in linear algebra and matrix transformation.</li><li>Acquire technical material, effectively present it and objectively evaluate other technical materials in linear algebra.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">B. Cognitive skills</span></strong><br></p><p style="text-align:justify;">Students should be able to demonstrate that they can:</p><ol><li>Produce descriptions and explanations of the different types of matrices and linear operations.</li><li>Apply their understanding of the studied ideas in linear algebra to coding problems, encryption and decryption.</li><li>Use knowledge gained from the module to help them to understand new unfamiliar matrix operations.&nbsp;&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></p><p style="text-align:justify;">Students should be able to:</p><ol><li>Communicate effectively in English and Arabic in a variety of contexts and media.</li><li>Analyze a mass of information and carry out an appropriate analysis of the problem material.</li><li>Express a problem in mathematical terms and carry out an appropriate analysis.</li><li>Reason critically and interpret information in a manner that can be communicated effectively.</li><li>I&ZeroWidthSpace;ntegrate and link information across course components.</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">D. Key transferable skills&nbsp;</span></strong><br></p><p>Students should be able to demonstrate that they can:</p><ol><li>Communicate complex information, arguments and ideas effectively and without plagiarism on a range of topics relating to linear operations.</li><li>Perform calculations to find inverse of a matrix, use and manipulate simple algebraic calculations to solve linear system of equations.</li><li>Use technology to find a span and a basis for a vector space.</li><li>Enhance existing numerical ability.</li><li>Work effectively as part of a group in solving any complicated mathematical problems.&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;<br><br></li></ol><p><br></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    M251&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Object Oriented Programming using Java <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module is intended to provide students a good understanding of object-oriented principles, including inheritance, polymorphism, class libraries, interacting objects, and the unified modelling language (UML). It uses the JAVA language to illustrate theses principles.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_11">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_11" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Object Oriented Programming using Java</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>M251</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Object Oriented Programming using Java</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module is intended to provide students a good understanding of object-oriented principles, including inheritance, polymorphism, class libraries, interacting objects, and the unified modelling language (UML). It uses the JAVA language to illustrate theses principles.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul><li>&ZeroWidthSpace;Introduce all aspects of object-oriented principles</li><li>Identifying and implementing class relationships using abstract classes, interfaces and inheritance</li><li>Provide knowledge in using simple UML class diagrams</li><li>&nbsp;Describe how these concepts are implemented in java</li><li>Provide knowledge in how to explore the JAVA API and to develop your own</li><li>&nbsp;Provide the knowledge necessary to construct java programs</li><li>&nbsp;Describe a number of the advanced facilities of java including exceptions </li><li>Show how java can be used in developing non-trivial programs</li><li>Introduce good design and programming practice<br><br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After studying the module, <strong>the student will be able to&nbsp;</strong>demonstrate:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">An understanding of the object-oriented principles</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Some knowledge of the main constructs and mechanisms in Java</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">An appreciation of the implications of object oriented software analysis and design</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">An understanding of the techniques used in developing a large Java program</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>B. Cognitive skills</strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After studying the module, <span style="text-decoration:underline;"><strong>the student will be able to</strong></span>:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Describe and apply key concepts and techniques in software design and development</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Analyze and abstract away from the details of a problem</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Design and formulate an appropriate solution to a problem and evaluate it&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After studying the module, <strong>the student will be able to</strong>:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Assemble, program, develop, debug, test and evaluate software systems<br></span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use software tools such as a Java IDE </span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use good design and programming practice</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Develop and implement class relationships&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After studying the module, <strong>the student will be able to</strong>:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Find information from a range of sources to support a task </span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Plan complex tasks </span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use new Java libraries </span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use appropriate numerical, mathematical and abstraction skills </span></li><li><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Progress to more advanced level studies&ZeroWidthSpace;&ZeroWidthSpace;</span><br><br></span></li></span></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    M257&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Programming using Java <span class="float-right">(5) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module is intended to provide students a good understanding of object-oriented principles, including inheritance, polymorphism, class libraries, interacting objects, and the unified modelling language (UML). It uses the JAVA language to illustrate theses principles.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_97">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_97" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Programming using Java</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>M257</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Programming using Java</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>M253</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>5</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module is intended to provide students a good understanding of object-oriented principles, including inheritance, polymorphism, class libraries, interacting objects, and the unified modelling language (UML). It uses the JAVA language to illustrate theses principles.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p></p><ul><li>&ZeroWidthSpace;Introduce all aspects of object-oriented principles</li><li>Identifying and implementing class relationships using abstract classes, interfaces and inheritance</li><li>Provide knowledge in using simple UML class diagrams</li><li>&nbsp;Describe how these concepts are implemented in java</li><li>Provide knowledge in how to explore the JAVA API and to develop your own</li><li>&nbsp;Provide the knowledge necessary to construct java programs</li><li>&nbsp;Describe a number of the advanced facilities of java including exceptions</li><li>Show how java can be used in developing non-trivial programs</li><li>Introduce good design and programming practice&ZeroWidthSpace;<br><br></li></ul><p>&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;</p><div><table class="ms-formtable" border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-top:8px;"><tbody><tr><td valign="top" class="ms-formbody" width="350px"><div aria-labelledby="ctl00_ctl39_g_eb7daa64_36cc_4108_a9f5_cc8a9db927e9_ctl00_ctl05_ctl09_ctl00_ctl00_ctl05_ctl00_label" style="display:inline;"><p><span class="ms-rteThemeFontFace-1">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1">After studying the module,&nbsp;<strong>the student will be able to&nbsp;</strong>demonstrate:</span></p><ol><li><span class="ms-rteThemeFontFace-1">An understanding of the object-oriented principles</span></li><li><span class="ms-rteThemeFontFace-1">Some knowledge of the main constructs and mechanisms in Java</span></li><li><span class="ms-rteThemeFontFace-1">An appreciation of the implications of object oriented software analysis and design</span></li><li><span class="ms-rteThemeFontFace-1">An understanding of the techniques used in developing a large Java program</span></li></ol><p><span class="ms-rteThemeFontFace-1"><strong>B. Cognitive skills</strong><br></span></p><p><span class="ms-rteThemeFontFace-1">After studying the module,&nbsp;<span style="text-decoration-line:underline;"><strong>the student will be able to</strong></span>:</span></p><ol><li><span class="ms-rteThemeFontFace-1">Describe and apply key concepts and techniques in software design and development</span></li><li><span class="ms-rteThemeFontFace-1">Analyze and abstract away from the details of a problem</span></li><li><span class="ms-rteThemeFontFace-1">Design and formulate an appropriate solution to a problem and evaluate it&ZeroWidthSpace;</span></li></ol><p><span class="ms-rteThemeFontFace-1"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1">After studying the module,&nbsp;<strong>the student will be able to</strong>:</span></p><ol><li><span class="ms-rteThemeFontFace-1">Assemble, program, develop, debug, test and evaluate software systems<br></span></li><li><span class="ms-rteThemeFontFace-1">Use software tools such as a Java IDE</span></li><li><span class="ms-rteThemeFontFace-1">Use good design and programming practice</span></li><li><span class="ms-rteThemeFontFace-1">Develop and implement class relationships&ZeroWidthSpace;</span></li></ol><p><span class="ms-rteThemeFontFace-1"><strong><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1">After studying the module,&nbsp;<strong>the student will be able to</strong>:</span></p><ol><li><span class="ms-rteThemeFontFace-1">Find information from a range of sources to support a task</span></li><li><span class="ms-rteThemeFontFace-1">Plan complex tasks</span></li><li><span class="ms-rteThemeFontFace-1">Use new Java libraries</span></li><li><span class="ms-rteThemeFontFace-1">Use appropriate numerical, mathematical and abstraction skills</span></li><li><span class="ms-rteThemeFontFace-1">Progress to more advanced level studies&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;</span></li></ol></div></td></tr></tbody></table></div><p><br></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    M269&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Algorithms, Data structures and Computability. <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    One of the basic pillars of advanced computing projects consists of the set of proper algorithms used to solve not only traditional but also unconventional IT problems. With the huge amount of data embedding the new data science, being skilled in setting proper data structure, managing and understanding computability techniques become a must nowadays. M269 is one of the most important modules for information technologies and computing related majors and tracks. The underlying concepts of this module are implemented using the python programming language.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_12">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_12" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Algorithms, Data structures and Computability.</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>M269</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Algorithms, Data structures and Computability.</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>One of the basic pillars of advanced computing projects consists of the set of proper algorithms used to solve not only traditional but also unconventional IT problems. With the huge amount of data embedding the new data science, being skilled in setting proper data structure, managing and understanding computability techniques become a must nowadays. M269 is one of the most important modules for information technologies and computing related majors and tracks. The underlying concepts of this module are implemented using the python programming language.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul><li>&ZeroWidthSpace;Provide the students with the required skills to possess the computational thinking. These skills start by proper understanding and analyzing the problems to be solved and end by providing computer programs that solve these problems.</li><li>One of the important aspects of this module is to provide the students with the awareness of the limits of computation and the ability to decide which problems can and which cannot be solved efficiently with computers.&ZeroWidthSpace;<br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong><br></p><p>Upon completing this module, students will be able to: </p><ol><li>Identify and define the sets, functions and logic, and their application in the design, implementation and analysis of computer-based systems.</li><li>Define and recognize Data structure and computational problematic.&ZeroWidthSpace;</li></ol><p><strong>B. Cognitive skills</strong><br></p><p>Upon completing this module, students will be able to: </p><ol><li>Explain, construct and use algorithms and data structures to solve computational problems. </li><li>Describe and assess the difficulty of computational problems. </li><li>A&ZeroWidthSpace;nalyse algorithms and computational problems making use of several informal proof techniques&nbsp;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></p><p>Upon completing this module, students will be able to: </p><ol><li>Use the Python programming language to implement algorithms. </li><li>Write a short report which is based on one or more sources and which has a well-argued conclusion.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">D. Key transferable skills&nbsp;</span></strong><br></p><p>Upon completing this module, students will be able to: </p><ol><li>Apply appropriate computational problem-solving techniques to a range of problems;</li><li>Apply computational thinking skills to solve problems across a range of application areas.</li><li>Discuss the questions 'What is computation?' and 'What are its limits?', and explain how the answers to these questions have important implications for the practical use of computer-based systems.</li></ol><p><br></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    M298&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Operating Systems <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The study of Operating Systems is essential since these are an integral part of modern IT systems. This is an introductory level module which introduces students to fundamental concepts of a variety of operating systems.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_96">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_96" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Operating Systems</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>M298</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Operating Systems</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>T103</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>The study of Operating Systems is essential since these are an integral part of modern IT systems. This is an introductory level module which introduces students to fundamental concepts of a variety of operating systems.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;</p><ul><li>Provide students extensive knowledge on OS in general, OS principles and modules and how their internals work and functions.</li><li>Provide key mechanisms in design of operating systems modules.</li><li>Introduce students to definitions of the Operating Systems such as OS control all of a computer's resources and present users with the equivalent of virtual machines that are easier to program than their underlying hardware.</li><li>Teach core operating systems concepts including operating system structure, process management, synchronization and concurrency, threads, memory management techniques, process scheduling and resource management, virtual memory concepts, deadlocks.</li><li>Give an overview of fundamental operating system principles, complemented with discussions of concrete modern systems to help students understand how these principles are applied in real OSs.</li><li>Enable students to compare performance of processor scheduling algorithms.</li><li>Teach students to produce algorithmic solutions to process synchronization problems.</li><li>Provide students with a good grasp of basic abstractions employed in system-level software (such as processes, threads, virtual memory, caching, etc.),</li><li>Teach students to use modern operating system calls such as Linux process and synchronization libraries.</li><li>Develop a sense in understand designing and implementing systems and working as part of a team.<br>&ZeroWidthSpace;&ZeroWidthSpace;<br><br></li></ul><p>&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;</p><div><table class="ms-formtable" border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-top:8px;"><tbody><tr><td valign="top" class="ms-formbody" width="350px"><div aria-labelledby="ctl00_ctl39_g_eb7daa64_36cc_4108_a9f5_cc8a9db927e9_ctl00_ctl05_ctl09_ctl00_ctl00_ctl05_ctl00_label" style="display:inline;"><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">A. Knowledge and understanding</span></strong><br></p><p>After completing this module, students will be able to:</p><ol><li>&nbsp;Identify and learn what operating systems are, what they do.</li><li>Describe How the Operating System are designed and constructed.</li><li>&nbsp;Show what the common features of an operating system are.</li><li>Explain what an operating system does for the user, and what it does&nbsp;&nbsp; for the computer-system operator.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">B. Cognitive skills</span></strong><br></p><p>After completing this module, students will be able to:</p><ol><li>Analyze the operating system design, constructor, building, internal&nbsp;&nbsp; works, usage variety, operations, and functions.</li><li>&nbsp;Demonstrate the basis for future work in other areas of OS: hacking Linux, i.e. contribute to the Open source OS, security and so on&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">C. Practical and professional skills</span></strong><br></p><p>After completing this module, students will be able to:</p><ol><li>Implement the design simple of Operating System structures.</li><li>Demonstrate basic skills to enable you to progress to more advanced level studies at the AOU or any other university.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">D. Key transferable skills&nbsp;</span></strong><br></p><p>After completing this module, students will be able to:</p><ol><li>Demonstrate study skills at a level appropriate to higher education, such as timetabling study; read critically for meaning and take effective notes; and use study aids such as dictionaries and glossaries;</li><li>Identify and distinguish between number of concepts that inform the Operating system structure components.</li><li>&nbsp;Communicate appropriately with your tutor and other students using email, online conferences and forums;</li><li>&nbsp;Locate information on a given subject from the World Wide Web.&ZeroWidthSpace;&ZeroWidthSpace;<br><br></li></ol></div></td></tr></tbody></table></div><p><br></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    MS101&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Physics <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    	
An understanding of the physical phenomena underlying the operation of devices involved in information processing and transmission can lead to better understanding of those devices.    In addition, software developers of computer games frequently require knowledge of the behavior of physical objects in order to produce realistic games.  Finally, as a fundamental science, a good understanding of physics and its techniques will help students develop a better understanding of nature and how to approach studying it.  The module has implicit links to computer communication and software development modules, in addition to the final year project.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_91">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_91" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Physics</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>MS101</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Physics</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>	
An understanding of the physical phenomena underlying the operation of devices involved in information processing and transmission can lead to better understanding of those devices.    In addition, software developers of computer games frequently require knowledge of the behavior of physical objects in order to produce realistic games.  Finally, as a fundamental science, a good understanding of physics and its techniques will help students develop a better understanding of nature and how to approach studying it.  The module has implicit links to computer communication and software development modules, in addition to the final year project.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;</p><ul><li>&ZeroWidthSpace;&ZeroWidthSpace;To impart knowledge and understanding of fundamental concepts of physics likely to be needed by the students for later modules and future careers.<br></li><li>To develop an appreciation of physics' tools and techniques for understanding the real world.</li><li>To develop transferrable problem-solving skills that can be applied in other areas.&ZeroWidthSpace;&ZeroWidthSpace;<br><br></li></ul><p>&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;</p><div><table class="ms-formtable" border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-top:8px;"><tbody><tr><td valign="top" class="ms-formbody" width="350px"><div aria-labelledby="ctl00_ctl39_g_eb7daa64_36cc_4108_a9f5_cc8a9db927e9_ctl00_ctl05_ctl09_ctl00_ctl00_ctl05_ctl00_label" style="display:inline;"><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong>&ZeroWidthSpace;&ZeroWidthSpace;</p><p>Upon completing this module, students will be able to:</p><ol><li><strong></strong>Explain the various important units of physics and the concept of dimensional analysis and the representation and manipulation of physical quantities</li><li>Outline the laws of classical mechanics</li><li>Contrast and differentiate among the different types of waves and summarize their properties</li><li>Explain electric forces and fields and summarize their properties</li><li><strong></strong>Illustrate and explain basic passive electric circuits<br><br></li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">B. Cognitive skills</span></strong><br></p><p>Upon completing this module, students will be able to:<br></p><ol><li>&nbsp;Identify concepts and quantities in physics precisely beyond what is used in everyday language.</li><li>Apply strategies for solving problems in physics in different situations.</li><li>Use vector algebra to the study of mechanics in two dimensions.</li><li>Analyze passive electric circuits.</li><li>Analyze wave propagation in different materials.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></p><p>Upon completing this module, students will be able to:</p><ol><li>Use and interpret different types of graphs to display the relationship between variables</li><li>Analyze the forces of static and dynamic bodies in simple mechanical systems</li><li>Calculate the velocity and acceleration of bodies in different types of plane motion</li><li>Determine basic parameters of waves propagating in different materials</li><li>Calculate voltages and currents in passive electric circuits&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">D. Key transferable skills&nbsp;</span></strong><br></p><p>Use the learning Management System (LMS) effectively to improve own learning performance.</p><ol><li>Demonstrate active participation and contribution to classroom discussions.</li><li>Improve own learning and performance through self-reflection.<br></li><li>Demonstrate effective communicate about technical matters.&ZeroWidthSpace;&ZeroWidthSpace;<br><br></li></ol></div></td></tr></tbody></table></div><p><br></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    MS102&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Physics <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    An understanding of the physical phenomena underlying the operation of devices involved in information processing and transmission can lead to better understanding of those devices.    In addition, software developers of computer games frequently require knowledge of the behavior of physical objects in order to produce realistic games.  Finally, as a fundamental science, a good understanding of physics and its techniques will help students develop a better understanding of nature and how to approach studying it.  The module has implicit links to computer communication and software development modules, in addition to the final year project.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_38">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_38" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Physics</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>MS102</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Physics</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>An understanding of the physical phenomena underlying the operation of devices involved in information processing and transmission can lead to better understanding of those devices.    In addition, software developers of computer games frequently require knowledge of the behavior of physical objects in order to produce realistic games.  Finally, as a fundamental science, a good understanding of physics and its techniques will help students develop a better understanding of nature and how to approach studying it.  The module has implicit links to computer communication and software development modules, in addition to the final year project.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul><li>&ZeroWidthSpace;&ZeroWidthSpace;To impart knowledge and understanding of fundamental concepts of physics likely to be needed by the students for later modules and future careers.<br></li><li>To develop an appreciation of physics' tools and techniques for understanding the real world.</li><li>To develop transferrable problem-solving skills that can be applied in other areas.&ZeroWidthSpace;<br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong>&ZeroWidthSpace;&ZeroWidthSpace;</p><p>Upon completing this module, students will be able to: </p><ol><li><strong></strong>Explain the various important units of physics and the concept of dimensional analysis and the representation and manipulation of physical quantities</li><li>Outline the laws of classical mechanics</li><li>Contrast and differentiate among the different types of waves and summarize their properties</li><li>Explain electric forces and fields and summarize their properties</li><li><strong></strong>Illustrate and explain basic passive electric circuits<br><br></li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">B. Cognitive skills</span></strong><br></p><p>Upon completing this module, students will be able to:<br></p><ol><li>&nbsp;Identify concepts and quantities in physics precisely beyond what is used in everyday language.</li><li>Apply strategies for solving problems in physics in different situations.</li><li>Use vector algebra to the study of mechanics in two dimensions.</li><li>Analyze passive electric circuits.</li><li>Analyze wave propagation in different materials.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></p><p>Upon completing this module, students will be able to: </p><ol><li>Use and interpret different types of graphs to display the relationship between variables</li><li>Analyze the forces of static and dynamic bodies in simple mechanical systems</li><li>Calculate the velocity and acceleration of bodies in different types of plane motion</li><li>Determine basic parameters of waves propagating in different materials</li><li>Calculate voltages and currents in passive electric circuits&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">D. Key transferable skills&nbsp;</span></strong><br></p><p>Use the learning Management System (LMS) effectively to improve own learning performance.</p><ol><li>Demonstrate active participation and contribution to classroom discussions.</li><li>Improve own learning and performance through self-reflection.<br></li><li>Demonstrate effective communicate about technical matters.&ZeroWidthSpace;<br></li></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    MT101&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;General Mathematics <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    General Mathematics provides students a college level academicexperience that emphasizestheuseofalgebraandfunctionsinproblemsolving andmodelling.It also provides a foundation in quantitative literacy,supplies the algebra and other mathematics needed in partner and subsequent disciplines. Thismodule isanintroductorylevelcoursewhich,inspecific, reviews various areas of college mathematicssuchaslinearequations, quadraticequations,rationalexpressions, analyticgeometry,solvingandgraphing inequalities, imaginarynumbers andsets.The coursealsointroduceselementary functionssuchas linear,quadratic,polynomial, exponential,and logarithmic.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_93">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_93" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">General Mathematics</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>MT101</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>General Mathematics</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>General Mathematics provides students a college level academicexperience that emphasizestheuseofalgebraandfunctionsinproblemsolving andmodelling.It also provides a foundation in quantitative literacy,supplies the algebra and other mathematics needed in partner and subsequent disciplines. Thismodule isanintroductorylevelcoursewhich,inspecific, reviews various areas of college mathematicssuchaslinearequations, quadraticequations,rationalexpressions, analyticgeometry,solvingandgraphing inequalities, imaginarynumbers andsets.The coursealsointroduceselementary functionssuchas linear,quadratic,polynomial, exponential,and logarithmic.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    MT129 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculus and Probability <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module introduces the concepts of differentiation and integration as well as some applications of differential and integral calculus. Moreover, the module offers a clear and comprehensive survey of the of data sampling, measurements of central tendency and spread, organizing and visualizing categorical and numerical data. It also includes topics in the basic probability such as events, simple probability, conditional probability, and Bayes’ rule. Finally, it provides an introduction to fundamental basis and concepts of statistical inferences, normal distribution. The module has direct links to computing, programming and communication modules, in addition to the numerical analysis module.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_49">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_49" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Calculus and Probability</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>MT129 </td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Calculus and Probability</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module introduces the concepts of differentiation and integration as well as some applications of differential and integral calculus. Moreover, the module offers a clear and comprehensive survey of the of data sampling, measurements of central tendency and spread, organizing and visualizing categorical and numerical data. It also includes topics in the basic probability such as events, simple probability, conditional probability, and Bayes’ rule. Finally, it provides an introduction to fundamental basis and concepts of statistical inferences, normal distribution. The module has direct links to computing, programming and communication modules, in addition to the numerical analysis module.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;<span style="text-align:justify;">&ZeroWidthSpace;The module aims to:</span></p><ul><li>Apply the knowledge of elementary functions to calculus concepts.</li><li>To compute the derivative of polynomials, rational, radical, trigonometric, exponential, and logarithmic functions.</li><li>Evaluate the integrals of polynomials, rational, radical, trigonometric, exponential, and logarithmic functions.</li><li>Introduce the terms and concept of probability, and the idea of discrete and continuous random variables.</li><li>Ensure the understanding of mathematical expectations and moment generating functions concepts.</li><li>Equip students with some important discrete and continuous probability distributions in technology and communication modules.&ZeroWidthSpace;<br><br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong><br></p><p>Students will be able to:</p><ol><li>Use derivative rule to find derivatives of power, exponential, logarithmic and trigonometric functions.</li><li>Solve simple definite and indefinite integrals.</li><li>Use applications of differentiation and integration in sketching graphs, obtain area between curves and average value of functions.</li><li>Define and identify random variables for any well- defined probability problems.&nbsp; </li><li>Realize mathematical expectations and variances for different continuous and discrete distribution&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">B. Cognitive skills</span></strong><br></p><p style="text-align:justify;">Students should be able to:</p><ol><li>Produce descriptions and explanations of the different types of elementary functions and apply their understanding of the studied functions to information systems.</li><li>Display deep knowledge gained from the course and use it to solve optimization problems.</li><li>Utilize knowledge gained from the course to help them to understand new unfamiliar probability distributions.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></p><p>Students will be able to:</p><ol><li>Apply the practical skills gained from differential and integral calculus ITC problems. </li><li>Cultivate the capacity to be leaders in their professional and personal communities.</li><li>Develop some technical statistical materials; effectively present and objectively evaluate them.</li><li>Deal with statistical computer applications such as spread sheets and MATLAB statistics toolbox.&ZeroWidthSpace;</li></ol><div><strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">D. Key transferable skills&nbsp;</span></strong></div><div><strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;"></span></strong><font face="arial, sans-serif"><span style="font-size:16px;"><b><br></b></span></font><p>Students will be able to:</p><ol><li>Be aware of the implications of information technology in daily lives and on society as a whole, and the ability to utilize IT to communicate and solve problems.</li><li>Use information, reasoning, and creative processes to solve problems and achieve goals.</li><li>Implement global issues gained from module and their implications on their daily lives.&ZeroWidthSpace;<br><br></li></ol></div></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    MT131&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Discrete Mathematics <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This is an elementary level module which introduces various topics in discrete mathematics. It offers a clear and comprehensive survey of logic operations, predicates, quantifiers, sets, functions, relations. Also, the module provides the concept of permutations, combinations and counting techniques which are needed as prerequisite in most of technology and communication modules. Moreover, the module gives some knowledge of relevant algorithmic ideas in number theory and cryptography that are widely used in data structure, data base, programming, data communication and in scientific research.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_1">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_1" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Discrete Mathematics</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>MT131</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Discrete Mathematics</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This is an elementary level module which introduces various topics in discrete mathematics. It offers a clear and comprehensive survey of logic operations, predicates, quantifiers, sets, functions, relations. Also, the module provides the concept of permutations, combinations and counting techniques which are needed as prerequisite in most of technology and communication modules. Moreover, the module gives some knowledge of relevant algorithmic ideas in number theory and cryptography that are widely used in data structure, data base, programming, data communication and in scientific research.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;The course aims to:<br></p><ul><li>Introduce basic notations used in&nbsp; discrete Mathematics associated with information and communication technology</li><li>Teach the rudiments of elementary mathematical reasoning.</li><li>Prepare students for the theoretical parts of further courses in information technology.</li><li>Explain logic from a mathematical perspective and relating it to computer applications.</li><li>Introduce set theory, relations, functions, graphs, equivalence relations, and partial orderings.</li><li>Provide concepts of permutation, combination and any other counting techniques.&ZeroWidthSpace;<br><br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong><br></p><p>Students will be able to:</p><ol><li>Identify propositional logic, logical equivalence, predicates and quantifiers.</li><li>Describe the Integers and division functions, prime number and prime factorization, least common multiple and highest common factors.</li><li>Define sets, functions and binary relations, their properties and representations. Know the major types of binary relations on a set, equivalence relations and partial orderings.</li><li>Use matrices to represent relations, graphs and trees. </li><li>Recognize basic properties of counting techniques using permutation and combination properties.&nbsp;&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">B. Cognitive skills</span></strong><br></p><p>Students will be able to:</p><ol><li>Deal with mathematical and logical arguments and carry out mathematical and logical manipulations.</li><li>Acquire a good understanding of the concepts and methods of discrete mathematics described in detail in the syllabus.</li><li>Be familiar with mathematical notations related to computer science.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></p><p>Students will be able to:</p><ol><li>Prove any simple mathematical theory using logic laws</li><li>Use any or all of the previous tools in a significant information and communication technology application such as cryptography. </li><li>Apply combinatorial principles and discrete mathematical structures that are central to mathematics and information technology.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">D. Key transferable skills</span></strong><br></p><p>Students will be able to:</p><ol><li>Demonstrate study skills at a level appropriate to higher education, such as timetabling study; read critically for meaning and take effective notes; and use study aids such as dictionaries and glossaries;</li><li>Present &nbsp;and communicate basic mathematical and logical arguments; communicate appropriately with their tutor and other students using email and online conferences;</li><li>Locate information on a given subject from the World Wide Web&ZeroWidthSpace;<br><br></li></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    MT132&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Linear Algebra <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The course introduces a range of ideas concerning matrices and its applications, matrix operations that are widely used in data structure, programming, data communication, digital signal processing and in scientific research. The course shows algorithmic method to solve systems of linear equations. Moreover, it includes concept of vector spaces and subspace that are used to construct algebraic codes. Also, it introduces the meaning of basis and dimension of a subspace the vector space Rn. The concept of linear transformation between two vector spaces together with null space and rank are also included. Finally, the course introduce the idea of characteristic values/vectors and diagonalization.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_2">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_2" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Linear Algebra</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>MT132</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Linear Algebra</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>The course introduces a range of ideas concerning matrices and its applications, matrix operations that are widely used in data structure, programming, data communication, digital signal processing and in scientific research. The course shows algorithmic method to solve systems of linear equations. Moreover, it includes concept of vector spaces and subspace that are used to construct algebraic codes. Also, it introduces the meaning of basis and dimension of a subspace the vector space Rn. The concept of linear transformation between two vector spaces together with null space and rank are also included. Finally, the course introduce the idea of characteristic values/vectors and diagonalization.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;<span style="text-align:justify;">T</span><span style="text-align:justify;">he course aims to:</span></p><ul><li>Extend the students' basic mathematical awareness and skills in matrices and matrix operations.</li><li>Give the study skills necessary for students to be able to solve system of linear equations. </li><li>Provide a range of useful ideas such as linear combinations and linear independence. </li><li>Present some important mathematical terms such as span, basis and dimensions.</li><li>Upgrade the concept of linear transformation necessary for other compulsory technology and communication modules.</li><li>Give a feeling for the mathematical approach to the study of computer science.&nbsp;<br><br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong><br></p><p>Student will be able to:</p><ol><li>Define and classify type of matrices and perform matrix operations.</li><li>Solve problems in information systems and communication using matrix techniques.</li><li>Use and apply linear algebra knowledge and concepts to information technologies and computing.</li><li>Be familiar with different terminologies in linear algebra and matrix transformation.</li><li>Acquire technical material, effectively present it and objectively evaluate other technical materials in linear algebra.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">B. Cognitive skills</span></strong><br></p><p style="text-align:justify;">Students should be able to demonstrate that they can:</p><ol><li>Produce descriptions and explanations of the different types of matrices and linear operations.</li><li>Apply their understanding of the studied ideas in linear algebra to coding problems, encryption and decryption.</li><li>Use knowledge gained from the module to help them to understand new unfamiliar matrix operations.&nbsp;&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></p><p style="text-align:justify;">Students should be able to:</p><ol><li>Communicate effectively in English and Arabic in a variety of contexts and media. </li><li>Analyze a mass of information and carry out an appropriate analysis of the problem material.</li><li>Express a problem in mathematical terms and carry out an appropriate analysis.</li><li>Reason critically and interpret information in a manner that can be communicated effectively.</li><li>I&ZeroWidthSpace;ntegrate and link information across course components.</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">D. Key transferable skills&nbsp;</span></strong><br></p><p>Students should be able to demonstrate that they can:</p><ol><li>Communicate complex information, arguments and ideas effectively and without plagiarism on a range of topics relating to linear operations.</li><li>Perform calculations to find inverse of a matrix, use and manipulate simple algebraic calculations to solve linear system of equations.</li><li>Use technology to find a span and a basis for a vector space. </li><li>Enhance existing numerical ability.</li><li>Work effectively as part of a group in solving any complicated mathematical problems.&ZeroWidthSpace;&ZeroWidthSpace;<br></li></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    MT372&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Parallel Computing <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The module is a comprehensive study of parallel computing techniques, parallel programming and performance tuning. Topics covered include: fundamentals of parallel, concurrent and distributed computing systems, performance and limitations of these systems, and parallelism paradigms. In addition to these topics the software needs and support for parallel processor systems are covered in details. This includes programming languages, simulation and tracing tools. Students will examine a range of topics involved in using parallel operations to improve computational performance, parallel architectures, parallel algorithms and parallel programming languages; Architectures covered include vector computers, multiprocessors, network computers, and data flow machines.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_39">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_39" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Parallel Computing</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>MT372</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Parallel Computing</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>The module is a comprehensive study of parallel computing techniques, parallel programming and performance tuning. Topics covered include: fundamentals of parallel, concurrent and distributed computing systems, performance and limitations of these systems, and parallelism paradigms. In addition to these topics the software needs and support for parallel processor systems are covered in details. This includes programming languages, simulation and tracing tools. Students will examine a range of topics involved in using parallel operations to improve computational performance, parallel architectures, parallel algorithms and parallel programming languages; Architectures covered include vector computers, multiprocessors, network computers, and data flow machines.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;<span style="text-align:justify;">&ZeroWidthSpace;The module aims to give solid understanding about the following:</span></p><ol><li>The fundamentals of parallel computing.</li><li>Parallel operation.</li><li>The different core concepts behind the hardware layer of a computer system.</li><li>Performance and limitations of parallel systems</li><li>The processor's architecture of parallel systems and its interconnection networks.</li><li>The parallel algorithms.&nbsp;&ZeroWidthSpace;<br></li></ol></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong><br></p><p>Upon completing this module, students will be able to:</p><ol><li>&nbsp;Understand of the fundamental concept and issues of parallel computing </li><li>Recognize &nbsp;parallel programming experience solving computationally intensive problems in a variety of disciplines</li><li>Understand the related implementations and measurements of performance and constraints of parallel computing&ZeroWidthSpace;</li></ol><p><strong>B. Cognitive skills</strong><br></p><p>Upon completing this module, students will be able to:</p><ol><li>Practice Parallel programming platforms </li><li>Apply Principles of parallel algorithm design</li><li>Illustrate Basic communication operations</li><li>Perform Analytical modelling of parallel programs</li><li>Develop Programming using the message-passing paradigm (MPI)&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></p><p>Upon completing this module, students will be able to:</p><ol><li>Apply the techniques and theorems in real applications.</li><li>Analyze specific data and information to build the parallel models</li><li>Apply the tools studied concerning parallel computing to solve a real problem.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">D. Key transferable skills&nbsp;</span></strong><br></p><p>Upon completing this module, students will be able to:<br></p><ol><li>Gather data from various sources, including the electronic media, such as internet.</li><li>Choose a case study from the real world and apply the techniques studied.</li><li>Show responsibility for the preparation of the case study and manage the presentation schedule of his/her work.</li><li>Exercise research skills, such as data collection, tabulation, analysis, report presentation and class discussions.&ZeroWidthSpace;<br><br></li></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    MT380 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Service oriented architecture <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Service-Oriented Architecture (SOA) intends to explain the SOA and the related topics including Web Services and Cloud Computing. Web Services (such as KSOAP, REST) make use of the notion of a service- oriented architecture, they are independent of specific programming languages or operating systems. They rely on existing transport technologies, such as HTTP, and XML, for invoking the implementation. This outlines a range of new technologies for designing and implementing service-oriented applications that support machine-to-machine collaboration. It illustrates the rational of SOA in how to construct and to build web service oriented applications, such as ASP.NET Web Service, Windows Communication Foundation (WCF), etc. to make use of knowledge about the research topics in SOA, and to discover future development trends.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_40">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_40" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Service oriented architecture</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>MT380 </td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Service oriented architecture</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Service-Oriented Architecture (SOA) intends to explain the SOA and the related topics including Web Services and Cloud Computing. Web Services (such as KSOAP, REST) make use of the notion of a service- oriented architecture, they are independent of specific programming languages or operating systems. They rely on existing transport technologies, such as HTTP, and XML, for invoking the implementation. This outlines a range of new technologies for designing and implementing service-oriented applications that support machine-to-machine collaboration. It illustrates the rational of SOA in how to construct and to build web service oriented applications, such as ASP.NET Web Service, Windows Communication Foundation (WCF), etc. to make use of knowledge about the research topics in SOA, and to discover future development trends.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;<span style="text-align:justify;">&ZeroWidthSpace;This Module discovers the concepts and technologies for the state of art topics: Service-Oriented Architecture (SOA) and Cloud Computing.&nbsp; It identify a comprehensive and systematic understanding to the latest SOA and Cloud Computing technologies. Moreover, it examine practical experience in designing large-scale composite web service applications.</span></p><p>After finishing successfully this Module you should be able to:<br></p><ul><li>Discover the benefit of using Service-Oriented Architecture to design modern software systems</li><li>Interpret the key features and building blocks of Web Service including WSDL, SOAP and UDDI</li><li>Develop programs using Microsoft .NET　and C# language</li><li>Apply service-based web application using ASP.NET and AJAX</li><li>Create service-oriented application using Windows Communication Foundation<br> build RESTful web service using Windows Communication Foundation</li><li>Outline the relationship between Cloud Computing and SOA; compare different cloud computing services&ZeroWidthSpace;<br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">A. Knowledge and understanding</span></strong><br></p><p>Upon completing this Module, students will be able to have:</p><ol><li>Construct a well-founded knowledge in the field of study.</li><li>Compare other disciplines that are related to the field of study.</li><li>Develop international perspective on the field of study.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">B. Cognitive skills</span></strong><br></p><p><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">Upon completing this Module, students will be able to:</span><br></p><ol><li>Collect, analyse and organise information and ideas and to convey those ideas clearly and fluently, in both written and spoken forms.&nbsp;&nbsp; </li><li>Interact effectively with others in order to work towards a common outcome.&nbsp; </li><li>Select and use the appropriate level, style and means of communication.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </li><li>Engage effectively and appropriately with information and communication technologies.<br></li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;"><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">C. Practical and professional skills</span></strong><br></span></strong></p><p>Upon completing this Module, students will be able to:</p><ol><li>Develop programs using Microsoft .NET and C# and service-based web application using ASP.NET and AJAX</li><li>Build service-oriented application using Windows Communication Foundation</li><li>Build RESTful web service using Windows Communication Foundation<br></li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;"><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">D.&nbsp;Key transferable skills&nbsp;</span></strong><br></span></strong></p><p>Upon completing this Module, students will be able to:</p><ol><li>Work and learn independently.&nbsp;&nbsp;&nbsp; </li><li>Generate ideas and adapt innovatively to changing environments.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </li><li>&ZeroWidthSpace;Identify problems creates solutions, innovate and improve current practices&ZeroWidthSpace;<br></li></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    MT390&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Image Processing <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Image Processing is an important field of study and MT390 is meant to provide students with the basic knowledge of this field.  Along with the importance of Image Processing in traditional areas such as Medical Diagnosis, Industrial Inspections, Security Systems, Robotics etc., the pervasiveness of smart phones equipped with powerful cameras has increased the need for Image Processing due to the availability of large amount of image data. This module is intended to provide students the opportunity to study the basics of the important field of Image Processing.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_41">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_41" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title"> Image Processing</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>MT390</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td> Image Processing</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Image Processing is an important field of study and MT390 is meant to provide students with the basic knowledge of this field.  Along with the importance of Image Processing in traditional areas such as Medical Diagnosis, Industrial Inspections, Security Systems, Robotics etc., the pervasiveness of smart phones equipped with powerful cameras has increased the need for Image Processing due to the availability of large amount of image data. This module is intended to provide students the opportunity to study the basics of the important field of Image Processing.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;The aims of this module are to:<br></p><ul><li>Introduce students to the important field of Image Processing.</li><li>Teach students the fundamental concepts related to image Representations and Enhancements.</li><li>Impart to the students knowledge about Intensity Transformations and Spatial Domain Filtering.</li><li>Introduce students to the concepts of 2-D Fourier Transform and the basics of Frequency Domain Filtering.</li><li>Introduce students to the topics of Image Segmentation, Image Coding and their related techniques.</li><li>Enable students to implement basic image processing algorithms using the Matlab Programming environment.<br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong><br></p><p style="text-align:justify;">On successful completion of this course, the student will be able to demonstrate knowledge and understanding of:</p><ol><li>Basic image representation concepts.</li><li>Spatial domain image processing techniques of intensity transformation and filtering.</li><li>Frequency domain image processing techniques of filtering and masking.</li><li>Data reduction and image coding methods.</li><li>Basic image segmentation concepts and techniques.<br></li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">B. Cognitive skills</span></strong><br></p><p style="text-align:justify;">On successful completion of this course, the student will be able to:<br></p><ol><li>Critically evaluate and suggest spatial domain processing techniques for image enhancement purposes.</li><li>Analyse and suggest appropriate frequency domain filtering techniques suitable for image processing tasks.</li><li>Critically interpret histogram data of images and suggest appropriate image processing techniques for image enhancement.</li><li>Analyze various image coding techniques and select the appropriate one for a particular task.</li><li>Evaluate and interpret image segmentation results.</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></p><p>On successful completion of this course, the student will be able to:</p><ol><li>Apply skills and concepts from the course to develop practical image processing projects.</li><li>Develop, Interpret and Implement image enhancement techniques both in the spatial and frequency domains.</li><li>Perform Matlab simulations of practical image processing algorithms including image enhancement, coding and segmentation.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">D. Key transferable skills&nbsp;</span></strong><br></p><p>On successful completion of this course, the student will be able to:</p><ol><li>Apply the mathematical and algorithmic skills acquired in this course to other areas of study and work.</li><li>Carry out independent learning on topics related to image processing and computing.</li><li>Communicate ideas and concepts about image processing techniques effectively both in writing as well as in any group discussion or environment.&ZeroWidthSpace;<br><br></li></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    MT395&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Applied Cyber Security <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    In today’s world, organizations must be prepared to defend against threats in cyberspace. Decision makers must be familiar with the basic principles and best practices of cyber security to best protect their enterprises.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_42">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_42" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Applied Cyber Security</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>MT395</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Applied Cyber Security</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>In today’s world, organizations must be prepared to defend against threats in cyberspace. Decision makers must be familiar with the basic principles and best practices of cyber security to best protect their enterprises.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;The aims and objectives of this module are to:<br></p><ul><li>Describe and discuss a range of topics in cyber security management.</li><li>Describe cyber security governance and the implementation of an integrated security mechanism.</li><li>Identify cyber security threats and explain risk analysis and management.</li><li>Allow students to perform independent research in the area and to critically read and analyse third party material.<br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong><br></p><p>After studying the module you will be able to:<br></p><ol><li>Describe cyber security fundamentals </li><li>Explain cyber security management and its importance to organizations</li><li>Evaluate the principles of cyber security governance to sustain and improve the security posture of an organisation</li><li>&nbsp;Interpret the importance of risk analysis and management in protecting an organization from cyber threats</li><li>&nbsp;Evaluate cyber security management policies, standards, and processes</li><li>Define the most common cyber security threats and analyse appropriate countermeasures</li><li>Describe and discuss the application of an integrated security mechanism&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">B. Cognitive skills</span></strong><br></p><ol><li>Recognise and define the main issues and challenges related to protecting and safeguarding organisations from cyber security risks</li><li>Read, evaluate, and critically review technical documents and extract useful information from these documents on topics related to cyber security, risk management, threat detection and countermeasures<br></li></ol><div><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></div><div><p>After studying the module you will be able to:</p><ol><li>&nbsp;Use the studied concepts to analyse and assess the cyber security risks</li><li>Identify the threats to information security and take appropriate countermeasures&nbsp;&ZeroWidthSpace;</li></ol><strong>D. Key transferable skills</strong><br></div><div><ol><li>Demonstrate independent self-learning capabilities in order to tackle more advanced topics and remain up-to-date in the field of cyber security<br></li><li>Employ your technical writing skills on topics related to cyber security and cyber security management<br></li></ol></div></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    SL101&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Spanish for Beginners (I) <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    	
The course introduces the student to the basics of Spanish. These include the alphabet, common everyday expressions, simple sentences, short dialogues and small paragraphs. The four skills of reading, writing, listening and speaking will be equally emphasized. However, as we live in the age of the image, students will have ample exposure to a variety of audio-visual material which boost their command of the language at the beginner’s level. The communicative approach is to be adopted in face-to-face tutorials and the various methods of enabling students to learn on their own will be prioritized.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_88">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_88" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Spanish for Beginners (I)</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>SL101</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Spanish for Beginners (I)</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>	
The course introduces the student to the basics of Spanish. These include the alphabet, common everyday expressions, simple sentences, short dialogues and small paragraphs. The four skills of reading, writing, listening and speaking will be equally emphasized. However, as we live in the age of the image, students will have ample exposure to a variety of audio-visual material which boost their command of the language at the beginner’s level. The communicative approach is to be adopted in face-to-face tutorials and the various methods of enabling students to learn on their own will be prioritized.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    SL102&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Spanish for Beginners (II) <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The course builds on what the student has learnt in level (1). Toward this end, it introduces the student to more everyday expressions, more widely-used short sentences, some compound and complex sentences, medium-size dialogues, and short passages. While the skills of listening and speaking will be receiving adequate attention, more emphasis is to be placed on the skills of reading and writing. Face-to-face tutorials will be communicative and students will be empowered to learn on their own.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_89">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_89" class="modal fade" role="dialog" style="display: none;" aria-hidden="true">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Spanish for Beginners (II)</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>SL102</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Spanish for Beginners (II)</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>SL101</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>The course builds on what the student has learnt in level (1). Toward this end, it introduces the student to more everyday expressions, more widely-used short sentences, some compound and complex sentences, medium-size dialogues, and short passages. While the skills of listening and speaking will be receiving adequate attention, more emphasis is to be placed on the skills of reading and writing. Face-to-face tutorials will be communicative and students will be empowered to learn on their own.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    T103&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Computer Organization and Architecture <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module offers a clear and comprehensive survey about computer organization and architecture. It introduces the inner workings of a modern digital computer through an integrated presentation of fundamental concepts and principles

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_99">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_99" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Computer Organization and Architecture</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>T103</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Computer Organization and Architecture</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>EL111</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module offers a clear and comprehensive survey about computer organization and architecture. It introduces the inner workings of a modern digital computer through an integrated presentation of fundamental concepts and principles
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;</p><div><table class="ms-formtable" border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-top:8px;"><tbody><tr><td valign="top" class="ms-formbody" width="350px"><div aria-labelledby="ctl00_ctl39_g_eb7daa64_36cc_4108_a9f5_cc8a9db927e9_ctl00_ctl05_ctl07_ctl00_ctl00_ctl05_ctl00_label" style="display:inline;"><p>&ZeroWidthSpace;To emphasize on the concept of computer organization.<br></p><p>To emphasize on the concept computer architecture.</p><p>To comprehend the different core concepts behind the hardware layer of a computer system.</p><p>To recognize the mathematical concepts of the low level computer structure (circuits and gates).</p><p>To know the processor's instruction sets architecture and implementation.</p><p>To recognize the memory organization concept and methods<br><br></p></div></td></tr></tbody></table></div><p>&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;</p><p><span class="ms-rteThemeFontFace-1">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1">The module provides student with an understanding of:</span></p><ol><li><span class="ms-rteThemeFontFace-1">Historical developments of computers.</span></li><li><span class="ms-rteThemeFontFace-1">The Von-Neumann Model.</span></li><li><span class="ms-rteThemeFontFace-1">Data representation and arithmetic in Computer Systems.</span></li><li><span class="ms-rteThemeFontFace-1">Boolean Algebra and Digital Logic.</span></li><li><span class="ms-rteThemeFontFace-1">Assembly language of an intuitive architecture (MARIE).</span></li><li><span class="ms-rteThemeFontFace-1">Memory organization and addressing modes.</span></li><li><span class="ms-rteThemeFontFace-1">Cache memory mapping Schemes.</span></li></ol><p><span class="ms-rteThemeFontFace-1"><strong>B. Cognitive skills</strong><br></span></p><p><span class="ms-rteThemeFontFace-1"><strong>To be able to</strong><br></span></p><ol><li><span class="ms-rteThemeFontFace-1">Identify the different parts of any computer system and understand their roles.</span></li><li><span class="ms-rteThemeFontFace-1">Understand the instruction set of any modern computer system.</span></li><li><span class="ms-rteThemeFontFace-1">&ZeroWidthSpace;Evaluate the performance of modern computer systems.</span></li></ol><p><span class="ms-rteThemeFontFace-1"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1"><strong>To be able to</strong><br></span></p><ol><li><span class="ms-rteThemeFontFace-1">Have an awareness of the process of designing, writing and testing&nbsp; MARIE assembly programs.</span></li><li><span class="ms-rteThemeFontFace-1">Use low level programming skills appropriate to a task.</span></li><li><span class="ms-rteThemeFontFace-1">Ability to use the MARIE and data path simulator software.</span></li></ol><p><span class="ms-rteThemeFontFace-1"><strong><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1"><strong>To be able to</strong></span></p><ol><li><span class="ms-rteThemeFontFace-1">Interact effectively within a group using electronic conferencing techniques.</span></li><li><span class="ms-rteThemeFontFace-1">Contribute to discussions on a conference.</span></li><li><span class="ms-rteThemeFontFace-1">Improve own learning and performance.</span></li><li><span class="ms-rteThemeFontFace-1">Communicate effectively about testing strategies, design and low level codes.</span></li><li>Use electronic media (the web and electronic conferencing) for information retrieval and communication.&ZeroWidthSpace;&ZeroWidthSpace;<br><br></li></ol><p><br></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    T215A&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Communication and Information Technologies A <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Students will begin with Communication and information technologies (T215) – learning about the core principles upon which new technologies are built. They will gain an understanding of the ways in which data is stored, manipulated and transmitted; and discover how new processes and services are transforming our lives.

Digital communication and information technologies have become fundamental to the operation of modern societies. New products and services are rapidly transforming our lives, both at work and at play. 
	
This module will help students learn more about these developments, and will equip them with the understanding and skills to continue learning about new developments in the future. Students will study the core principles on which the technologies are built and, through a range of online and offline activities, investigate new topics and technologies. 

After studying this module, students will be in a better position to appreciate the potential of developments in communication and information technologies.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_13">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_13" class="modal fade" role="dialog" style="display: none;" aria-hidden="true">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Communication and Information Technologies A</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>T215A</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Communication and Information Technologies A</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Students will begin with Communication and information technologies (T215) – learning about the core principles upon which new technologies are built. They will gain an understanding of the ways in which data is stored, manipulated and transmitted; and discover how new processes and services are transforming our lives.

Digital communication and information technologies have become fundamental to the operation of modern societies. New products and services are rapidly transforming our lives, both at work and at play. 
	
This module will help students learn more about these developments, and will equip them with the understanding and skills to continue learning about new developments in the future. Students will study the core principles on which the technologies are built and, through a range of online and offline activities, investigate new topics and technologies. 

After studying this module, students will be in a better position to appreciate the potential of developments in communication and information technologies.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul><li>&ZeroWidthSpace;To introduce students to modern topics in ICTs.</li><li>To develop student's skills in managing technologies of data storage and computer networks.</li><li>To develop students skills in the technologies of mobile communication systems with an emphasis on mobile telephony.&ZeroWidthSpace;<br><br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong><br></p><p>Upon completing this module, students should be able to: </p><ol><li>Describe key principles and concepts of digital communication and information systems and their component devices, including such topics as LANs, WLANs, mobile communication networks, encoding, modulation, multiplexing, routing, and standards.</li><li>Explain key principles and concepts relating to digital data including the storage, manipulation and transmission of digital data.</li><li>Identify major trends in communication and information technologies.</li><li>Enhance their scientific reading and writing skills for writing short reports.<br></li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">B. Cognitive skills</span></strong><br></p><p>Upon completing this module, students should be able to:</p><ol><li>Produce descriptions and explanations of the communication and information systems that feature in the module and of their underlying technologies and component devices</li><li>Apply their understanding of the communication and information systems that feature in the module, their underlying technologies and component devices in specified contexts, updating themselves about the systems, technologies and devices as necessary.</li><li>Use knowledge gained from the module to help them to figure out new or unfamiliar communication and information systems in specified situations; describe and explain such systems and their technologies and devices; apply their understanding in specified contexts.</li><li>Analyze and discuss some of the technological, social, legal, ethical and personal issues that relate to communication and information systems, technologies and devices.</li><li>Realize an overview of the way in which mobile telephone systems have developed from its first generation till LTE stage.&ZeroWidthSpace;<br></li></ol><div><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></div><div><br></div><p>Upon completing this module, students should be able to:</p><ol><li>Critique draft materials in order to improve them</li><li>Use standard office and communication software effectively to support their work</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">D. Key transferable skills&nbsp;</span></strong><br></p><p>Upon completing this module, students should be able to:</p><ol><li>Communicate complex information, arguments and ideas effectively and without plagiarism on a range of topics relating to communication and information systems through a variety of different media, using styles, language and images appropriate to purpose, audience and medium</li><li>Perform simple calculations relating to communication and information systems, use and manipulate simple algebraic equations and interpret and produce graphical and tabular data</li><li>Use information technology to find information from various sources and evaluate that information</li><li>Develop a range of skills as an independent learner to support them in learning through the module materials and through other resources that they seek out for themselves.&ZeroWidthSpace;<br></li></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    T215B&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Communication and Information Technologies B <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Digital communication and information technologies have become fundamental to the operation of modern societies. New products and services are rapidly transforming our lives, both at work and at play. This module will help you to learn more about these developments through studying the core principles on which the technologies are built and, through a range of online and offline activities, investigate new topics and technologies.

This module will also help you to raise students’ awareness of some of the technologies and issues associated with safeguarding the privacy of digital information and the people who are affected by its use – hence the themes ‘protecting’ and ‘prying’.

These themes are explored through case studies and practical examples. A recurring approach is the use of an analytical framework that uses five themes to examine the technologies and issues: convenience, identity, reliability, acceptability and consequences.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_14">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_14" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Communication and Information Technologies B</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>T215B</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Communication and Information Technologies B</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Digital communication and information technologies have become fundamental to the operation of modern societies. New products and services are rapidly transforming our lives, both at work and at play. This module will help you to learn more about these developments through studying the core principles on which the technologies are built and, through a range of online and offline activities, investigate new topics and technologies.

This module will also help you to raise students’ awareness of some of the technologies and issues associated with safeguarding the privacy of digital information and the people who are affected by its use – hence the themes ‘protecting’ and ‘prying’.

These themes are explored through case studies and practical examples. A recurring approach is the use of an analytical framework that uses five themes to examine the technologies and issues: convenience, identity, reliability, acceptability and consequences.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul><li>Increase the knowledge of the basic principles of communication and information systems and technologies, and the issues relating to their use</li><li>Develop the ability to apply the understanding of communication and information technologies to learn about new or unfamiliar systems and technologies</li><li>Enable students to explore how personal and private data can be protected.</li><li>Help students develop an understanding of audio and video encoding and editing.</li><li>Develop a variety of skills appropriate to a practitioner in communication and information technologies.&ZeroWidthSpace;</li></ul><p><br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this module, students should be able to: </span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Describe key principles and concepts relating to digital data including the availability of, mechanisms for protecting digital personal data, and the associated privacy and security issues related to it.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Explain major trends of the fastest expanding areas of ICT, that of audio and video production and its potential for entertaining us.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Understand key concepts, issues and technologies associated with online communication.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Enhance the scientific reading and writing skills for writing long reports.<br></span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>B. Cognitive skills</strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this module, students should be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Produce descriptions and explanations of the fundamental building block of all modern security systems which is encryption.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Apply their understanding of the themes of security framework for communication and information systems that feature in the module, their underlying technologies and component devices for applying biometrics as a measurement of human beings used to identify them in the context of authentication. </span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use knowledge gained from the module to help them to figure out new or unfamiliar topics; conveying information in audio and visual format, introduction for some tools that will assist in obtaining a simple digital video from a number of digital still images.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Describe and discuss some of the technological, social, legal, ethical and personal issues that relate to securing personal data like preventing unauthorized people from having access to private information.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Evaluate or compare communication and information systems suggested for a particular need and give a justified recommendation on their appropriateness&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this module, students should be able to:</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Critique draft materials in order to improve them</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Experiment with some fingerprint recognition tools and evaluate the system using the given data set.</span></li><li><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use specialised software tools as AviSynth script language to provide the students with basic skills required to produce video from still images.&ZeroWidthSpace;</span><br></span></li></span></ol><p><br></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    T216A&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Cisco networking (CCNA)-A <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Students will begin with Cisco networking (CCNA) (T216). This will give them
the knowledge, understanding, and skills needed to configure a LAN/WAN using Cisco equipment (which should also leave you well prepared for the industry-standard CCNA certification examination) They will also gain hands-on practical experience of configuring networks at four compulsory day schools. 

Cisco Systems are market leaders in supplying networking equipment for the internet. They also have a well-established educational programme for network professionals. 

The Arab Open University offers the Cisco Certified Network Associate “CCNA” (ICND1) Version 5 curriculum, which provides the knowledge, understanding, and skills needed to configure a LAN/WAN using Cisco equipment.

The module is composed of two modules:
•	Introduction to Networks 
•	Routing and switching essentials
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_15">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_15" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title"> Cisco networking (CCNA)-A</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>T216A</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td> Cisco networking (CCNA)-A</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Students will begin with Cisco networking (CCNA) (T216). This will give them
the knowledge, understanding, and skills needed to configure a LAN/WAN using Cisco equipment (which should also leave you well prepared for the industry-standard CCNA certification examination) They will also gain hands-on practical experience of configuring networks at four compulsory day schools. 

Cisco Systems are market leaders in supplying networking equipment for the internet. They also have a well-established educational programme for network professionals. 

The Arab Open University offers the Cisco Certified Network Associate “CCNA” (ICND1) Version 5 curriculum, which provides the knowledge, understanding, and skills needed to configure a LAN/WAN using Cisco equipment.

The module is composed of two modules:
•	Introduction to Networks 
•	Routing and switching essentials</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul><li>&ZeroWidthSpace;Provide the student with the knowledge, understanding, and skills needed to configure a LAN/WAN using Cisco equipment.</li><li>Provide the student with hands-on experience of configuring networks.<br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong><br></p><p>After studying the module the student will be able to:<br></p><ol><li>Describe the role of protocol layers in data networks, and describe the devices and services used to support communications in data networks and the Internet&nbsp;</li><li>Describe the importance of addressing and naming schemes at various layers of data networks in IPv4 and IPv6 environments<br></li><li>Describe Ethernet and basic switching concepts, as well as the operation of Cisco switches<br></li><li>Explain enhanced switching technologies such as VLANs, VLAN Trunking Protocol (VTP), Rapid Spanning Tree Protocol (RSTP), Per VLAN Spanning Tree Protocol (PVSTP), and 802.1q<br></li><li>Describe the purpose, nature, and operations of a router, routing tables, and the route lookup process<br></li><li>Describe how VLANs create logically separate networks and how routing occurs between them<br></li><li>Describe dynamic routing protocols, distance vector routing protocols, and link-state routing protocols<br></li><li>Describe the operations and benefits of access control lists (ACLs) Dynamic Host Configuration Protocol (DHCP) and Domain Name System (DNS), and Network Address Translation (NAT)</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">B. Cognitive skills</span></strong><br></p><p>After studying the module the student will be able to:</p><ol><li>Design, calculate, and apply subnet masks and addresses to fulfil given requirements in IPv4 and IPv6 network</li><li>Build simple Ethernet network using routers and switches</li><li>Troubleshoot and monitor networks&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;"><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></span></strong></p><p>After studying the module the student will be able to:</p><ol><li>Build a simple Ethernet network using routers and switches&nbsp;</li><li>Use Cisco command-line interface (CLI) commands to perform basic router and switch configurations</li><li>Utilize common network utilities to verify small network operations and analyze data traffic</li><li>&nbsp;Configure, monitor and troubleshoot: basic operations of a small switched network, static routing, default routing, basic operations of routers in a small routed network (RIPv1, RIPv2 and OSPF protocols (single-area OSPF)), VLANs, inter-VLAN routing, ACLs for IPv4 and IPv6, and NAT&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;"><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">D. Key transferable skills&nbsp;</span></strong><br></span></strong></p><p>After studying the module the student will be able to:</p><p></p><ol><li>Build simple LANs, perform basic configurations for routers and switches, and implement IP addressing schemes.<br></li><li>Configure and troubleshoot routers and switches, and resolve common issues with RIPv1, RIPv2, virtual LANs, and inter-VLAN routing in both IPv4 and IPv6 networks.&ZeroWidthSpace;<br></li></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    T216B&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Cisco networking (CCNA)-B <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Cisco Systems are market leaders in supplying networking equipment for the internet. They also have a well-established educational programme for network professionals. 

The Arab Open University offers the Cisco Certified Network Associate “CCNA” (ICND2) Version 5 curriculum, which provides the knowledge, understanding, and skills needed to configure a LAN/WAN using Cisco equipment.

The module is composed of two modules:
•	Scaling Networks 
•	Connecting networks 

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_16">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_16" class="modal fade" role="dialog" style="display: none;" aria-hidden="true">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title"> Cisco networking (CCNA)-B</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>T216B</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td> Cisco networking (CCNA)-B</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Cisco Systems are market leaders in supplying networking equipment for the internet. They also have a well-established educational programme for network professionals. 

The Arab Open University offers the Cisco Certified Network Associate “CCNA” (ICND2) Version 5 curriculum, which provides the knowledge, understanding, and skills needed to configure a LAN/WAN using Cisco equipment.

The module is composed of two modules:
•	Scaling Networks 
•	Connecting networks 
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul><li>Provide the student with knowledge, understanding, and skills needed to configure a LAN/WAN using Cisco equipment.</li><li>Provide the student with hands-on experience of configuring networks.<br><br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong class="ms-rteThemeFontFace-1" style="font-size:13px;"><span lang="EN-GB">A. Knowledge and understanding</span></strong></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After studying the module the student will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&nbsp;Describe the operations and benefits of the Spanning Tree Protocol (STP)</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Describe the operations and benefits of link aggregation and Cisco VLAN Trunk Protocol (VTP)</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Describe the operations and benefits of EtherChannel and HSRP.&nbsp;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Explain the operations and benefits of Open Shortest Path First (OSPF) protocol (single-area OSPF and multi-area OSPF)&nbsp;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Explain the operations and benefits of Enhanced Interior Gateway Routing Protocol (EIGRP)</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&nbsp;Describe the different WAN technologies and their benefits</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&nbsp;Explain the operations and benefits of Standard and Extended Access control list (ACL).</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">xplain the common LAN security threats and how to mitigate them&ZeroWidthSpace;<br></span></li></span></ol><div><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">B. Cognitive skills</span></strong><br></span></div><div><span style="font-size:13px;"><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After studying the module the student will be able to:<br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Troubleshoot networks<br></span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Design network architectures for borderless networks, data centers and virtualization, and collaboration technology and solutions.&nbsp;&ZeroWidthSpace;</span></li></span></ol><strong class="ms-rteThemeFontFace-1" style="font-size:13px;"><span lang="EN-GB">C. Practical and professional skills</span></strong><br class="ms-rteThemeFontFace-1"></span></div><div><span style="font-size:13px;"><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After studying the module the student will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&nbsp;Configure and troubleshoot STP, RSTP, VTP, Extended VLAN, DTP, EtherChannel, HSRP, First Hop Redundancy Protocol, basic operations of routers in a complex routed network for IPv4 and IPv6, advanced operations of routers for IPv4 and IPv6, OSPF, and EIGRP .</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Configure and troubleshoot serial connections, broadband connections, ACL and IPSec tunnelling operations</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Monitor and troubleshoot network operations using syslog, SNMP, and NetFlow&ZeroWidthSpace;</span></li></span></ol><strong class="ms-rteThemeFontFace-1" style="font-size:13px;"><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong><br class="ms-rteThemeFontFace-1"></span></div><div><span style="font-size:13px;"><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After studying the module the student will be able to:</span></p><p>&nbsp;</p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Configure and troubleshoot routers and switches. He will also resolve common issues with OSPF, EIGRP, STP, and VTP in both IPv4 and IPv6 networks. In addition, he will also develop the knowledge and skills needed to implement an EtherChannel. </span></li><li><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Understand the selection criteria of network devices and WAN technologies to meet network requirements. Furthermore, he will learn how to configure and troubleshoot network devices and resolve common issues with data link protocols. Finally, he will also develop the knowledge and skills needed to implement IPSec and virtual private network (VPN) operations in a complex network.</span><br></span></li></span></ol></span></div></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    T227&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Change, strategy and projects at work <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module will improve students’ understanding of the origins, nature and consequences of change in the workplace. It also equips them with the knowledge, skills and competencies needed to successfully plan real practical projects. Besides, it allows students to gain an understanding of how ICTs both drive and enable change in the workplace. Moreover, it develops their knowledge, understanding and skills in project working and helps them to apply their new skills and knowledge to the planning of their own project involving the use of ICTs and associated business systems in their workplace.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_17">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_17" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title"> Change, strategy and projects at work</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>T227</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td> Change, strategy and projects at work</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module will improve students’ understanding of the origins, nature and consequences of change in the workplace. It also equips them with the knowledge, skills and competencies needed to successfully plan real practical projects. Besides, it allows students to gain an understanding of how ICTs both drive and enable change in the workplace. Moreover, it develops their knowledge, understanding and skills in project working and helps them to apply their new skills and knowledge to the planning of their own project involving the use of ICTs and associated business systems in their workplace.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul><li>Gain an understanding of how social, technological, economic, environmental, political, legislative and ethical factors drive and enable change in the workplace.</li><li>Develop knowledge, understanding, confidence and &ZeroWidthSpace;competence in project working and related employability skills</li><li>Evaluate, develop and review personal, academic and professional skills</li><li>Apply skills and knowledge to planning and presenting a project proposal that is capable of being implemented in their workplace.<br><br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Identify, analyse and explain the factors driving change in the workplace and the opportunities for introducing change, along with the associated challenges and consequences in terms of human and other factors.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Understand and explain the processes involved in designing, planning, monitoring, implementing and reviewing work-based projects.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Make effective use of appropriate information and communication technologies, and understand and explain their role in planning and communicating information relating to a work-based project designed to implement some aspect of workplace change.&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>B. Cognitive skills</strong><br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Apply knowledge and understanding effectively to a range of issues, questions and problems arising from the planning of a work-based project.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Explore, analyse and evaluate practical ways of improving workplace practices using appropriate information and communication technologies to develop components of a personal work-based project.&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use the workplace to learn, practise and develop your professional competence.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use appropriate information and communication technologies in a professional context.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Plan, organise your time and work effectively.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Review, analyse and record ongoing learning needs to maintain and develop skills in the context of the workplace using appropriate information and communication technologies.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&nbsp;Develop an awareness of ethical issues relevant to the workplace.&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong><br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Plan, monitor and evaluate your study as an independent learner.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use appropriate information and communication technologies to support your own learning.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Identify, critically assess and use information or data accurately in a range of contexts.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Communicate information, arguments and ideas effectively using technologies, styles and language appropriate to purpose and audience.</span></li><li><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Critically compare, analyse and use a variety of approaches appropriate to understanding issues or problems arising in the context of workplace change and projects.&ZeroWidthSpace;</span><br><br></span></li></span></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    T316&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Advanced Networking <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    With the continuous advancements in the networking field, the need arises for teaching advanced networking concepts. This advanced undergraduate course aims to meet this objective by discussing advanced networking topics complementing those introduced in T216A/B. 
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_22">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_22" class="modal fade" role="dialog" style="display: none;" aria-hidden="true">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title"> Advanced Networking</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>T316</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td> Advanced Networking</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>With the continuous advancements in the networking field, the need arises for teaching advanced networking concepts. This advanced undergraduate course aims to meet this objective by discussing advanced networking topics complementing those introduced in T216A/B. </td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul><li>&ZeroWidthSpace;Describe the various wireless networks along with their coexistence, cooperation, and interaction, while introducing a system level approach and providing an overview of recent research topics.</li><li>Describe the concepts of sensor networks along with their underlying challenges, including power efficiency, routing, and multihop communications</li><li>Discuss the challenges related to massive machine type communications inherent in large sensor networks deployments under the internet of things (IoT) paradigm).</li><li>Explain the concepts of software defined networks (SDN) and network function virtualization (NFV).</li><li>Define big data and describe its use in cloud computing.</li><li>Discuss cloud computing issues, and analyse the role of mobile clouds. </li><li>Define and discuss quality of experience (QoE) requirements, and compare and contrast QoE with quality of service (QoS).</li><li>Teach students the concepts of large data centres, data mining, their relation to big data, and explain data management and backup techniques.</li><li>Explain advanced network management and administration topics, such as: self-organizing networks, network planning and design, and advanced routing. </li><li>Equip students with advanced skills in personal updating and researching in the field of advanced networking. Students will be taught how to use third-party material in order to extract useful information for their personal and professional development<br><br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After studying the course you will be able to:<br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&nbsp;Describe and analyse the operation of co-existing wireless networks and the possibilities of cooperation and interaction between these networks</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&nbsp;Discuss the role of sensor networks and machine-to-machine communications (M2M) in the internet of things (IoT) and describe the underlying challenges</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&nbsp;Describe the concepts of software defined networks (SDN) and network function virtualization (NFV), and discuss their role in advanced network management and administration</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Discuss advanced routing concepts, such as the Border Gateway Protocol (BGP)</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Discuss Cloud Computing and Big Data concepts</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Differentiate between QoE and QoS, and discuss QoE metrics for specific applications, e.g. voice (VoIP) and video</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Describe the operation of self-organizing networks (SON), and differentiate between self-configuration, self-optimization, and self-healing&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">B. Cognitive skills</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After studying the course you will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Analyse the interaction between different technologies and networks in a complex setup involving multiple networks<br></span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Analyse the challenges faced by the different networks and assess the required techniques for enhancing the performance metrics (QoS, QoE, energy efficiency, security, etc.) of the various network types studied in the course<br></span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Read, evaluate, and critically review advanced technical documents and extract useful information from these documents on a specific networking topic&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After studying the course you will be able to:<br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use the studied concepts to analyse and assess the operation of complex networks<br></span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Design and plan basic implementations of the advanced networks studied, and assess the management and operation of these networks, including the use of self-organization techniques<br></span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Design QoE measurement and resource allocation techniques for enhancing QoE performance of networks using the studied concepts</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><span lang="EN-GB">Be ready to tackle complex
networking scenarios through self-learning and research skills coupled with the
learned course material</span>&ZeroWidthSpace;<br></span></li></span></ol><div><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong><br></span></div><div><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB"><br></span></strong></span></div><div><span style="font-size:13px;"><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After studying the course you will be able to:<br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Become an independent self-learner in order to remain up-to-date with the continuous advancements in the field of advanced networking<br></span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Improve your technical writing skills on topics related to networking and advanced networking</span></li></span></ol><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;"><br></span></strong></span></div><p></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    T318&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Applied Network Security <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    People, organizations, and enterprises are becoming increasingly dependent on digital services. Therefore, the need arises to protect information from being maliciously intercepted, disrupted, or misused. 
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_23">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_23" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Applied Network Security</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>T318</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Applied Network Security</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>People, organizations, and enterprises are becoming increasingly dependent on digital services. Therefore, the need arises to protect information from being maliciously intercepted, disrupted, or misused. </td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul><li>Define the threats to network security, and describe the differences between them.</li><li>Describe encryption techniques, including symmetric and asymmetric encryption methods.</li><li>Explain the most widely used encryption algorithms and standards, with focus on wireless, cloud, and internet security.</li><li>Equip students to be able to assess and manage network security risks, and implement appropriate countermeasures.</li><li>Allow students to perform independent research in the area and to critically read and analyse third party material.<br><br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong><br></p><p>After studying the course you will be able to:<br><br></p><ol><li>Describe the operation of encryption techniques: symmetric and asymmetric ciphers, block and stream ciphers<br></li><li>&nbsp;Define and explain the differences between different encryption algorithms and standards<br></li><li>Analyse and compare the performance of different encryption methods<br></li><li>Design and implement encryption algorithms</li><li>Describe the protocols for physical, network, and transport level security</li><li>Define the most common threats to network and internet security, explain their operation, and discuss their differences</li><li>&nbsp;Describe the protocols and countermeasures used for protecting network and internet traffic&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">B. Cognitive skills</span></strong><br></p><p>After studying the course you will be able to:<br></p><ol><li>Recognise the threats to network security and assess their inherent risks&nbsp;</li><li>Read, evaluate, and critically review technical documents and extract useful information from these documents on topics related to network security and cryptography algorithms<br></li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></p><p>After studying the course you will be able to:<br></p><ol><li>Use the studied concepts to implement, analyse, and assess different encryption algorithms and techniques<br></li><li>Identify the threats to network security and take appropriate countermeasures&nbsp;<br></li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">D. Key transferable skills&nbsp;</span></strong><br></p><p>After studying the course you will be able to:<br></p><ol><li>Become an independent self-learner in order to tackle more advanced topics and remain up-to-date in the field of network security<br></li><li>Improve your technical writing skills on topics related to cryptography and network security<br></li></ol><p><br></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    T390&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Computer Networks and Network Security <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    In today’s world, organizations must be prepared to defend against threats in cyberspace. Decision makers must be familiar with the basic principles and best practices of cyber security to best protect their enterprises.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_92">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_92" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Computer Networks and Network Security</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>T390</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Computer Networks and Network Security</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>In today’s world, organizations must be prepared to defend against threats in cyberspace. Decision makers must be familiar with the basic principles and best practices of cyber security to best protect their enterprises.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM103&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Computer Organization and Architecture <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module offers a clear and comprehensive survey about computer organization and architecture. It introduces the inner workings of a modern digital computer through an integrated presentation of fundamental concepts and principles
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_3">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_3" class="modal fade" role="dialog" style="display: none;" aria-hidden="true">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Computer Organization and Architecture</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM103</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Computer Organization and Architecture</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module offers a clear and comprehensive survey about computer organization and architecture. It introduces the inner workings of a modern digital computer through an integrated presentation of fundamental concepts and principles</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;To emphasize on the concept of computer organization.<br></p><p>To emphasize on the concept computer architecture.</p><p>To comprehend the different core concepts behind the hardware layer of a computer system.</p><p>To recognize the mathematical concepts of the low level computer structure (circuits and gates).</p><p>To know the processor's instruction sets architecture and implementation.</p><p>To recognize the memory organization concept and methods<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">The module provides student with an understanding of: </span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Historical developments of computers.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">The Von-Neumann Model.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Data representation and arithmetic in Computer Systems.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Boolean Algebra and Digital Logic.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Assembly language of an intuitive architecture (MARIE).</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Memory organization and addressing modes. </span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Cache memory mapping Schemes.</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>B. Cognitive skills</strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>To be able to</strong><br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Identify the different parts of any computer system and understand their roles.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Understand the instruction set of any modern computer system.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;Evaluate the performance of modern computer systems.</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>To be able to</strong><br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Have an awareness of the process of designing, writing and testing&nbsp; MARIE assembly programs.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use low level programming skills appropriate to a task.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Ability to use the MARIE and data path simulator software.</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>To be able to</strong></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Interact effectively within a group using electronic conferencing techniques.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Contribute to discussions on a conference.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Improve own learning and performance.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Communicate effectively about testing strategies, design and low level codes.</span></li></span><li>Use electronic media (the web and electronic conferencing) for information retrieval and communication.&ZeroWidthSpace;</li></ol><p><br></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM105&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Introduction to Programming <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module is an introductory level programming module and it is meant to provide basic foundation in computer programming to students. Students will learn how to develop solutions (algorithms) using pseudocode to solve simple problems. Thereafter, they will learn how to implement these solutions using a programming language (Java). This module serves as foundation for second level programming modules. 
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_4">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_4" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Introduction to Programming</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM105</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Introduction to Programming</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module is an introductory level programming module and it is meant to provide basic foundation in computer programming to students. Students will learn how to develop solutions (algorithms) using pseudocode to solve simple problems. Thereafter, they will learn how to implement these solutions using a programming language (Java). This module serves as foundation for second level programming modules. </td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;<strong>The module aims to:</strong></p><ul><li>Introduce the technique of solving simple problems using pseudocode.</li><li>Introduce Java programming via writing, compiling and executing simple programs.</li><li>Present how to store and deal with data including variables, constants, and expressions.</li><li>Cover deeply the concepts of program control structure and illustrate each concept with a diagrammatic notation using UML.</li><li>Present how these concepts are implemented in Java.</li><li>Introduce the concept of modularization and how to write Java methods.</li><li>Present how to deal with basic data structures like strings, arrays and two dimensional arrays.<br><br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">A. Knowledge and understanding</span></strong><br></p><p><strong>After studying the module, </strong><strong>the student will be able to</strong><strong>:</strong></p><ol><li>Understanding of the design and programming processes </li><li>Knowledge of the main constructs and mechanisms in programming using Java language. </li><li>Understanding of the techniques used in developing a medium Java application. </li><li>Understanding of the basic data structures like strings, arrays and two dimensional arrays.</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;">B. Cognitive skills</span></strong><br></p><p><strong>After studying the module, </strong><strong>the student should be able to</strong><strong>: </strong></p><ol><li>Describe and apply key concepts and techniques in software design and development.</li><li>Analyse and abstract away from the details of a problem.</li><li>Design and formulate an appropriate solution to a problem and evaluate it.</li><li>Deal professionally with the basic data structures.</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;">C. Practical and professional skills</span></strong><br></p><p><strong>After studying the module, </strong><strong>the student should be able to</strong><strong>: </strong></p><ol><li>Create, develop and trace Java programs. </li><li>Use software tools such as a Java IDE and an On-line Java compiler. </li><li>Use appropriate programming skills. </li><li>Traverse data in the basic data structures in a professional way.&nbsp;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;">D. Key transferable skills&nbsp;</span></strong><br></p><p><strong>After studying the module, </strong><strong>the student should be able to</strong><strong>: </strong></p><ol><li>Find information from a range of sources to support a task. </li><li>Plan medium tasks.</li><li>Use Java libraries.</li><li>Use appropriate numerical, mathematical and abstraction skills.&nbsp;<br></li></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM111 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Introduction to Computing and Information Technology 1 <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This is an introductory level 1 module, which provides students with a broad introduction to Computing and Information Technology concepts, principles and theories.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_5">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_5" class="modal fade" role="dialog" style="display: none;" aria-hidden="true">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Introduction to Computing and Information Technology 1</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM111 </td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Introduction to Computing and Information Technology 1</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This is an introductory level 1 module, which provides students with a broad introduction to Computing and Information Technology concepts, principles and theories.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul style="list-style-type:disc;"><li>Help students to develop their understanding about the significant role of computers in our lives.</li><li>Explore some processes by which sound and images in the real world are captured and stored and may be shared with peers and the wider world through social networking sites.</li><li>Introduce students to algorithmic thinking and problem-solving skills using examples from everyday life. </li><li>Enhance student's knowledge about implementing solutions to simple problems in a visual programming.</li><li>Introduce students to the key concepts and technologies underpinning the communication networks.</li><li>Prepare the student for further academic study by helping him develop his study skills.<br></li></ul><p><br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Understand the fundamental principles, concepts and techniques underlying Computing and IT.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Explore various situations in which Computing and IT systems are used, the ways in which people interact with them, and the possibilities and limitations of such systems </span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Be aware of the ethical, social and legal issues that can be associated with the development and deployment of Computing &amp; IT systems.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Demonstrate an understanding of algorithmic thinking and problem-solving skills using examples from everyday life. </span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Understand the general principles, roles of various components, and the challenges involved in sending data across communication networks.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Know how to find, rank and reference information; how to build your information literacy skills and how to interpret data in different forms.&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>B. Cognitive skills</strong><br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Evaluate key computing and IT concepts in a range of contexts.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Apply appropriate techniques and tools for abstracting, modelling, problem solving, designing and testing computing and IT systems.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Compare, contrast, critically analyze and refine specifications and implementations of software systems and/or simple hardware systems.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Identify situations in which different network technologies may be used.<br></span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Communicate information, arguments, ideas and issues clearly and in appropriate ways, bearing in mind the audience for and the purpose of your communication.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use appropriate numerical and mathematical skills to carry out calculations and analyze data.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Work independently, planning, monitoring, reflecting on and improving your own learning</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Demonstrate study skills at a level appropriate to higher education, such as study planning, learning from feedback and reading actively&nbsp;<br></span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">D Key transferable skills&nbsp;</span></strong><br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Evaluate computing and IT systems, using appropriate simulation and modelling tools where appropriate</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use a range of resources to help you develop as an independent learner.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use information literacy skills, computers and software packages appropriate to the workplace.</span></li><li><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Communicate appropriately with your tutor and other students using email, online conferences and forums.&ZeroWidthSpace;&ZeroWidthSpace;</span><br></span></li></span></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM112&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Introduction to Computing and Information Technology 2 <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module will further develop and extend the skills and knowledge that students will have built up by studying its partner module TM111. The overall focus of TM112 is on developing the students’ problem solving skills.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_6">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_6" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Introduction to Computing and Information Technology 2</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM112</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Introduction to Computing and Information Technology 2</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module will further develop and extend the skills and knowledge that students will have built up by studying its partner module TM111. The overall focus of TM112 is on developing the students’ problem solving skills.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul style="list-style-type:disc;"><li>&ZeroWidthSpace;Help students to practice the use of computing and information technologies to solve problems.</li><li>Explore a variety of information technologies, from basic computer architecture, cloud computing, mobile/wireless and location-based computing Introduces the students to algorithmic thinking and problem-solving skills using examples from everyday life. </li><li>Enhance student's knowledge about implementing solutions to simple problems in a visual programming.</li><li>Focus on how to examine computing and information technology problems and solutions in their real-world context, with a focus on information security </li><li>&ZeroWidthSpace;Develop numeracy skills (including algebra) in the context of information technologies and programming activities</li><li>Prepare the student for further academic study by helping him develop his study skills<br><br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Understand the fundamental principles, concepts and techniques underlying Computing and IT.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Identify &nbsp;a range of models to support the analysis and design of Computing and IT systems</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Know how to implement solutions to simple problems using Python programming language.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Be aware of the of the range of situations in which Computing and IT systems are used, the ways in which people interact with them, and the possibilities and limitations of such systems </span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Understand&nbsp; the ethical, social and legal issues that can be associated with the development and deployment of Computing &amp; IT systems</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Describe major trends in Computing and IT and of the implications of these trends&nbsp;&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>B. Cognitive skills</strong><br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Evaluate key computing and IT concepts in a range of contexts.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Apply appropriate techniques and tools for abstracting, modelling, problem solving, designing and testing computing and IT systems.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Compare, contrast, critically analyze and refine specifications and implementations of software systems and/or simple hardware systems.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Carry out a project in computing and IT that applies and extends student's knowledge and understanding, and critically reflect on the processes involved and the outcomes of student's work.<br></span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Communicate information, arguments, ideas and issues clearly and in appropriate ways, bearing in mind the audience for and the purpose of your communication.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use appropriate numerical and mathematical skills to carry out calculations and analyze data.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Work independently, planning, monitoring, reflecting on and improving your own learning</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Demonstrate study skills at a level appropriate to higher education, such as study planning, learning from feedback and reading actively&nbsp;<br></span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong><br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Evaluate computing and IT systems, using appropriate simulation and modelling tools where appropriate</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use a range of resources to help you develop as an independent learner.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use information literacy skills, computers and software packages appropriate to the workplace.</span></li><li><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Communicate appropriately with your tutor and other students using email, online conferences and forums.</span><br><br></span></li></span></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM240&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Computer Graphics and Multimedia <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module targets to cope with the current advances in computer graphics and multimedia and providing clear and concise explanations of the basic concepts of computer graphics and multimedia. This module is expected to enable students to gain understanding of basics of modelling, viewing, animation principles in both 2D and 3D and the impact of such topics on modern multimedia aspects.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_18">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_18" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title"> Computer Graphics and Multimedia</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM240</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td> Computer Graphics and Multimedia</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module targets to cope with the current advances in computer graphics and multimedia and providing clear and concise explanations of the basic concepts of computer graphics and multimedia. This module is expected to enable students to gain understanding of basics of modelling, viewing, animation principles in both 2D and 3D and the impact of such topics on modern multimedia aspects.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul><li>&ZeroWidthSpace;Introduce all aspects of the hardware and software components of computer graphics.</li><li>Provide Knowledge to perform 2D and 3D geometric transformations.</li><li>&nbsp;Describe the algorithms for projection, viewing and clipping of graphs.</li><li>Identify how to graphics software and hardware.</li><li>&nbsp;Provide Knowledge to evaluate the performance of graphics systems.&ZeroWidthSpace;<br><br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this module, <span lang="EN-GB"><strong>student should be able to:</strong></span></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Describe the basic principles of computer graphics.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Explain the different operations in graphics systems such as transformations, projects, views, texturing, lighting, shading, animation and clipping.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Select the suitable hardware and software of a graphics system for a specific application.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Explain graphics algorithms. </span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Develop graphics applications in Java.</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>B. Cognitive skills</strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this module, <span lang="EN-GB"><strong>student should be able to:</strong></span></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Evaluate graphics hardware and software.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Compare the different computer graphics applications.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Select the suitable graphics hardware for different applications.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Evaluate 3D modelling techniques.</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this module, <span lang="EN-GB"><strong>student should be able to:</strong></span></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Develop graphics applications using advanced APIs</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Apply computer graphics concepts and techniques to develop graphics and visualization applications</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Model 3D objects.<br></span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this module, <span lang="EN-GB"><strong>student should be able to:</strong></span></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Effectively communicate oral and written.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Work in a team.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;Effectively manage resources and time.</span></li></span></ol><p><br></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM260 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Security, ethics and privacy in IT and Computing <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The ITC specialists must conduct ethically by adhering to the ITC code of conduct  and understand the social, professional and legal context of IT and computing,
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_50">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_50" class="modal fade" role="dialog" style="display: none;" aria-hidden="true">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Security, ethics and privacy in IT and Computing</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM260 </td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Security, ethics and privacy in IT and Computing</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>The ITC specialists must conduct ethically by adhering to the ITC code of conduct  and understand the social, professional and legal context of IT and computing,</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;The module aims to:&nbsp; increase students awareness of the ethical, professional and legal issues of IT and computing and the responsible use of ITC.<br></p><p>Upon the successful completion of this module students will be able to:</p><ol style="list-style-type:decimal;"><li>Consider the ethical issues related to ITC systems.</li><li>Act ethically while making any profession related decisions.</li><li>Apply all legal principles to intellectual property and ITC related situation.</li><li>understand the emerging issues related to ethics in cyberspace</li><li>Develop a sound methodology in resolving ethical conflicts and crisis.</li><li>Understand the social and ethical issues in the professional practice of computing and technology and their impact on the society..</li><li>Look up relevant ethical standards as developed by the ACM.</li><li>State several examples of important ethical principles as they apply to computer science related situations.</li><li>Identify the ethical issues that relate to computer science in real situations they may encounter and decide whether a given action is ethical as regards computer science professional ethics, and justify that decision.</li><li>Research and write a professional-quality paper about a topic relating to social, legal, and ethical implications of computer science.&ZeroWidthSpace;<br><br></li></ol></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">A. Knowledge and understanding</span></strong><br></p><p>After completing this module, students will be able to: </p><ol><li>Understand how ITC could raise social issues and ethical dilemmas</li><li>Understand the historical background of some social, legal, philosophical, political, constitutional and economical issues related to ITC </li><li>&nbsp;Describe current social and legal developments related to computers and computer crime</li><li>Recognize the existence of computer abuse cases , laws pertaining to them </li><li>Appreciate the value of technology and identify the ethical and moral situations that must be faced and dealt with. </li><li>Deepen their understanding of technology and its effects on society.&ZeroWidthSpace;</li></ol><p><strong>B. Cognitive skills</strong><br></p><p>After completing this module, students will be able to:</p><ol><li>Evaluate the legal and professional impact of ITC in real life contexts</li><li>Analyse the effect of ethical issues on IT industry and society&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">C. Practical and professional skills</span></strong><br></p><p>After completing this module, students will be able to:</p><ol><li>Effectively identify and analyze professional and legal issues; </li><li>Promote an ethics of computing in practice;</li><li>Resolve dilemmas related to ethical, professional and legal ITC issues&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">D. Key transferable skills&nbsp;</span></strong><br></p><p>After completing this module, students will be able to: </p><ol><li>Communicate effectively in writing about ethical, legal and professional issues in the ITC context</li><li>&ZeroWidthSpace;Become an independent learner.<br><br></li></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM287&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Web Applications Development <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module provides key skills in using JavaScript/AJAX, PHP, and MySQL through demonstrating the vast possibilities they offer in developing robust code that complies with all modern web browsers. The module clarifies the roles of each of the client vs the server in web development and the importance of being able to have asynchronous calls and information exchange with focus on developing Web 2.0 applications.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_43">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_43" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Web Applications Development</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM287</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Web Applications Development</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module provides key skills in using JavaScript/AJAX, PHP, and MySQL through demonstrating the vast possibilities they offer in developing robust code that complies with all modern web browsers. The module clarifies the roles of each of the client vs the server in web development and the importance of being able to have asynchronous calls and information exchange with focus on developing Web 2.0 applications.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;The module aims to:<br></p><div><ol><li>Provide students with a full understanding the main components of web applications.</li><li>Introduce key technologies used for building dynamic web 2.0 applications (JavaScript/AJAX, PHP, and MySQL).</li><li>Emphasize the importance of using client-side technology (AJAX) to create asynchronous web applications.</li><li>Prepare the students for further academic study.&ZeroWidthSpace;<br></li></ol></div></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">A. Knowledge and understanding</span></strong><br></p><p>After studying this module, the student will be able to:</p><ol><li>Provide a solid understanding of how JavaScript is written and the possibilities it offers.</li><li>Develop the understanding to use JavaScript to improve the user experience.</li><li>Appreciate the importance of data validation before processing it.</li><li>Demonstrate how to use AJAX to post data to servers and process the feedback of the server.</li><li>Construct interactive web applications that integrate client-side and server-side programming using AJAX and PHP.</li><li>Learn the basics of MySQL and how to create tables to store, update and retrieve data that can be presented to the user using web technologies.</li><li>Use PHP on the server side to communicate with MySQL and generate dynamic content for the web.</li><li>Assess basic issues related to web design and how to improve the style of the generated web content.</li><li>Be able to combine all the technologies presented (JavaScript/AJAX, PHP, MySQL) into a single project that integrates all the components into one fully functional interactive web application.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">B. Cognitive skills</span></strong><br></p><p>After studying this module, the student will be able to:</p><ol><li>Evaluate websites based on the technologies they employ.</li><li>Analyse the performance of web applications.</li><li>Describe the importance of data validation specifically at the user-interface level of a computer system.</li><li>Describe the roles of each of the client and the server as used for web applications.</li><li>Design and build an appropriate system as a solution to data-centric problems.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;"><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">C. Practical and professional skills</span></strong><br></span></strong></p><p>After studying this module, the student will be able to:</p><ol><li>Develop robust and compact code that runs reliably in all modern Web browsers.</li><li>Develop the major components required for building modern web applications.</li><li>Demonstrate proficiency in applying the acquired programming skills to develop complex systems.</li><li>Develop simple user interfaces that collect data from the user to be validated and processed by computer systems.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;"><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">D. Key transferable skills&nbsp;</span></strong><br></span></strong></p><p>After studying this module, the student will be able to:</p><ol><li>Find, select and use information from a range of resources to support a specific task.</li><li>Develop and improve previously learnt programing skills to solve more complex tasks.</li><li>Plan and produce a modern system to satisfy the user needs whilst making sure to provide good stability and performance.</li><li>Plan and manage effort and progress whilst undertaking a substantial project.&ZeroWidthSpace;<br></li></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM290&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Cryptography and Internet Security <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Nowadays, people shop online, work online, play online. As our lives become increasingly dependent on digital services, the need arises to protect our personal information from being maliciously intercepted, disrupted, or misused.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_44">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_44" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Cryptography and Internet Security</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM290</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Cryptography and Internet Security</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Nowadays, people shop online, work online, play online. As our lives become increasingly dependent on digital services, the need arises to protect our personal information from being maliciously intercepted, disrupted, or misused.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;The aims and objectives of this module are to:<br></p><ul><li>Define the threats to network security, and describe the differences between them.</li><li>Describe encryption techniques, including symmetric and asymmetric encryption methods.</li><li>Explain the most widely used encryption algorithms and standards, with focus on internet security.</li><li>Allow students to perform independent research in the area and to critically read and analyse third party material.<br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong><br></p><p>Upon completing this module, students will be able to:<br></p><ol><li>Describe the operation of symmetric ciphers<br></li><li>Define and explain the differences between different encryption algorithms and standards</li><li>Describe the operation of asymmetric ciphers</li><li>Analyse and compare the performance of different encryption methods</li><li>Design and implement simple encryption algorithms</li><li>Define the most common threats to internet security, explain their operation, and discuss their differences</li><li>&nbsp;Describe the protocols and countermeasures used for protecting internet traffic&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">B. Cognitive skills</span></strong><br></p><p>Upon completing this module, students will be able to: </p><ol><li>Recognise the threats to online security&ZeroWidthSpace;</li><li>Read, evaluate, and critically review technical documents and extract useful information from these documents on topics related to cryptography and internet security</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></p><p>Upon completing this module, students will be able to: </p><ol><li>&nbsp;Use the studied concepts to analyse and assess the efficiency of different encryption standards</li><li>Identify the threats to internet security and take appropriate countermeasures&nbsp;&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">D. Key transferable skills&nbsp;</span></strong><br></p><p>Upon completing this module, students will be able to:</p><ol><li>Demonstrate independent self-learning capabilities in order to tackle more advanced topics and remain up-to-date in the field of cryptography and internet security</li><li>Employ your technical writing skills on topics related to cryptography and internet security&ZeroWidthSpace;<br><br></li></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM291&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Management Information System <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module introduces the use and relevance of information systems to managers and enterprises. Rather than providing an in depth technological treatment of information systems, this module prepares students as future managers to assess the impact of information systems on a particular enterprise. This module also introduces students to a range of skills required to manage information systems projects. It explores current Information Systems concepts and technologies. Students learn how information systems give a business or organization a competitive edge by providing technologies that help managers to plan, control and make decisions. 
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_45">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_45" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title"> Management Information System</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM291</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td> Management Information System</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module introduces the use and relevance of information systems to managers and enterprises. Rather than providing an in depth technological treatment of information systems, this module prepares students as future managers to assess the impact of information systems on a particular enterprise. This module also introduces students to a range of skills required to manage information systems projects. It explores current Information Systems concepts and technologies. Students learn how information systems give a business or organization a competitive edge by providing technologies that help managers to plan, control and make decisions. </td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;Aspects of business that were once seen in isolation – the people, organisation, process, information and technology – are now expected to operate as part of a seamless whole, both within and across enterprises. Information systems managers are responsible for delivering this seamless integration efficiency. This module aims to:<br></p><p>1. Explain basic concepts for IT/IS management </p><p>2. Discuss organizational, business and strategic issues surrounding IT/IS, and </p><p>3. Analyse and evaluate uses of strategic IT/IS in practice.<br><br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">A. Knowledge and understanding</span></strong><br></p><p>Upon completing this module, students should be able to: </p><ol><li>Define information, strategy and customer-facing (user-centred) design theories.</li><li>Compare the impact of different types of information technologies and systems in the enterprise and competitive environment.</li><li>Select information systems as a basis for sustainable competitive advantage.</li><li>Identify the issues that must be addressed in managing information systems projects and processes across various boundaries (organisational, cultural, legal and geographical).</li><li>Describe the life cycle methodologies and methods involved in developing and managing information systems in a global competitive environment.<br></li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">B. Cognitive skills</span></strong><br></p><p>Upon completing this module, students should be able to: </p><ol><li>Demonstrate a conceptual grasp of information, strategy and user-centred (customer-facing) design theories.</li><li>Distinguish between different types of information systems and recognise enterprise-wide, innovative methods of reducing costs and improving service through management information systems.</li><li>Compare and contrast the implications on the efficiency and effectiveness of different IT competitive strategies and their sustainability in the long term.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">C. Practical and professional skills</span></strong></p><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;"></span></strong></p><p>Upon completing this module, students should be able to: </p><ol><li>Reflect, analyse and interpret information on contemporary information systems management issues.</li><li>Debate controversial issues relating to information systems deployment in organisations&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">D. Key transferable skills&nbsp;</span></strong><br></p><p>Upon completing this module, students should be able to: </p><ol><li>Develop skills to effectively participate in a group. </li><li>Synthesise data and use application of concepts from other modules.</li><li>Improve case analysis skills.&ZeroWidthSpace;<br><br></li></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM295 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;System Modelling <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    System modelling is used as an essential part of the software development process; it also referred to as software modelling in this context. Models are built and analysed prior to the implementation of the system, and are used to direct the subsequent implementation. Modelling can be defined as considering the system from different views (or perspectives) in order to provide a better understanding of it. These views include (among others) requirements models, static models, and dynamic models of the software system. These different views can be further developed, understood, and communicated through the use of graphical modelling languages such as the Unified Modelling Language (UML).
The module focuses on how to use adequate models to express software at all levels of development; from the initial specification to implementation, with a special attention paid to UML.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_46">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_46" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">System Modelling</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM295 </td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>System Modelling</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>System modelling is used as an essential part of the software development process; it also referred to as software modelling in this context. Models are built and analysed prior to the implementation of the system, and are used to direct the subsequent implementation. Modelling can be defined as considering the system from different views (or perspectives) in order to provide a better understanding of it. These views include (among others) requirements models, static models, and dynamic models of the software system. These different views can be further developed, understood, and communicated through the use of graphical modelling languages such as the Unified Modelling Language (UML).
The module focuses on how to use adequate models to express software at all levels of development; from the initial specification to implementation, with a special attention paid to UML.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;&ZeroWidthSpace;</span><span class="ms-rteThemeFontFace-1" lang="EN-GB" style="font-size:13px;">&ZeroWidthSpace;This
module aims to introduce students to the software development process in
general with emphasis on the software modelling and analysis phase. The unified
modelling language is used throughout the module to illustrate the different
models.&nbsp; &nbsp;</span><br></span></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong><br></p><p>Upon completing this module, students will be able to: </p><ol><li>Describe the software engineering lifecycle and in particular the role of analysis and design phase in the lifecycle</li><li>Discuss the different software lifecycle models including (e.g., waterfall, agile)</li><li>Define the requirements elicitation and structuring</li><li>Explain how to use the UML models to develop and document software analysis and design artefacts.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">B. Cognitive skills</span></strong><br></p><p>Upon completing this module, students will be able to: </p><ol><li>Specify, analyse and organise requirements for a software product</li><li>Model, analyse and validate software requirements using UML and set-theoretic notations<br></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><span lang="EN-GB">Apply
appropriate UML design patterns and notations to the design of components of a
product</span>&ZeroWidthSpace;</span></li></ol><div><strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></div><div><p>Upon completing this module, students will be able to: </p><ol><li>Apply an appropriate software engineering process and tools to the task of structuring, modelling and validating requirements for a software product</li><li>Work independently, planning, monitoring, reflecting on and improving your own learning and working practices</li><li>work in a group, communicating computing ideas effectively in speech and in writing</li><li>&ZeroWidthSpace;Find, assess and apply information from a variety of sources, using information technology where necessary, in a number of assignments, including at least one significant piece of work&ZeroWidthSpace;</li></ol><strong><span lang="EN-GB" style="font-size:12pt;font-family:arial, sans-serif;">D. Key transferable skills&nbsp;</span></strong><br></div><div><p>Upon completing this module, students will be able to: </p><ol><li>Design software systems</li><li>Use modern software tools, both within and outside your workplace </li><li>Communicate effectively about software modelling and design</li><li>Be able to learn independently from third-party materials, in order to keep up to date in software engineering in general and software modelling in particular<br></li></ol></div><p></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM297&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compression Methods for Multimedia <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Data compression aims at finding new ways of representing data so that it takes very little storage, while still being able to reconstruct the original data from the compressed version. Compression is applied namely when storage space is at a premium or when data needs to be transmitted and bandwidth is at a premium (which always is the case). The most important thing about compression is that it is not ``one size fits all'' approach: essentially, compression aims at specifying the characteristics of the data that needs to be compressed (mainly looking for patterns to be explored in order to achieve compact data representation). This module defines a variety of data modeling and representation techniques, which is at the heart of compression. Recently, the convergence in the field of communications, computing and entertainment industries enabled data compression to be a part of everyday life (e.g. MP3, DVD and Digital TV) and has created a number of exciting new opportunities for new applications of compression technologies.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_47">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_47" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Compression Methods for Multimedia</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM297</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Compression Methods for Multimedia</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Data compression aims at finding new ways of representing data so that it takes very little storage, while still being able to reconstruct the original data from the compressed version. Compression is applied namely when storage space is at a premium or when data needs to be transmitted and bandwidth is at a premium (which always is the case). The most important thing about compression is that it is not ``one size fits all'' approach: essentially, compression aims at specifying the characteristics of the data that needs to be compressed (mainly looking for patterns to be explored in order to achieve compact data representation). This module defines a variety of data modeling and representation techniques, which is at the heart of compression. Recently, the convergence in the field of communications, computing and entertainment industries enabled data compression to be a part of everyday life (e.g. MP3, DVD and Digital TV) and has created a number of exciting new opportunities for new applications of compression technologies.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;The aims of this module are to illustrate methods for handling and compressing different kinds of data, such as text, images, audio and video data and show data compression techniques for multimedia and other applications, especially the once used in the Internet.<br></p><p>After finishing successfully this Module you should be able to:</p><ol style="list-style-type:decimal;"><li>Compute basic statistics of data.</li><li>Apply nontrivial algorithms to real-world problems.</li><li>Outline the principles of data compression.</li><li>Discover different compression methods for text, image, audio, and video data.</li><li>Extend different compression methods and their applications in different aspects of computing.<br><br></li></ol></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">A. Knowledge and understanding</span></strong><br></p><p>Upon completing this module, students will be able to: </p><ol><li>Develop a well-founded knowledge in the field of study.</li><li>Relate other disciplines to the field of study.</li><li>Develop an international perspective on the field of study.&ZeroWidthSpace;&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">B. Cognitive skills</span></strong><br></p><p><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" lang="EN-GB" style="font-size:13px;">Upon completing this module, students will be able to:&nbsp;</span><br></span></p><ol><li>Analyse and explore information and ideas and to convey those ideas clearly and fluently, in both written and spoken forms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </li><li>&ZeroWidthSpace;Experiment effectively with others in order to work towards a common outcome.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </li><li>Select and make use of appropriate level, style and means of communication.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </li><li>Experiment appropriately with information and communication technologies.</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">C. Practical and professional skills</span></strong><br></p><p>Upon completing this module, students will be able to: </p><ol><li>Apply different compression methods for text, image, audio, and video data</li><li>Examine nontrivial algorithms to real-world problems</li><li>Extend different compression methods and their applications in different aspects of computing.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">D. Key transferable skills&nbsp;</span></strong><br></p><p>Upon completing this module, students will be able to: </p><ol><li>Analyse and conclude independently.&nbsp;&nbsp;&nbsp;&nbsp; </li><li>Develop ideas and adapt innovatively to changing environments.</li><li>&nbsp;Identify problems constructs solutions, innovate and improve current practices&ZeroWidthSpace;<br><br></li></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM298&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Operating Systems <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The study of Operating Systems is essential since these are an integral part of modern IT systems. This is an introductory level module which introduces students to fundamental concepts of a variety of operating systems.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_19">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_19" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title"> Operating Systems</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM298</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td> Operating Systems</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>The study of Operating Systems is essential since these are an integral part of modern IT systems. This is an introductory level module which introduces students to fundamental concepts of a variety of operating systems.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul><li>Provide students extensive knowledge on OS in general, OS principles and modules and how their internals work and functions.</li><li>Provide key mechanisms in design of operating systems modules.</li><li>Introduce students to definitions of the Operating Systems such as OS control all of a computer's resources and present users with the equivalent of virtual machines that are easier to program than their underlying hardware.</li><li>Teach core operating systems concepts including operating system structure, process management, synchronization and concurrency, threads, memory management techniques, process scheduling and resource management, virtual memory concepts, deadlocks.</li><li>Give an overview of fundamental operating system principles, complemented with discussions of concrete modern systems to help students understand how these principles are applied in real OSs.</li><li>Enable students to compare performance of processor scheduling algorithms.</li><li>Teach students to produce algorithmic solutions to process synchronization problems.</li><li>Provide students with a good grasp of basic abstractions employed in system-level software (such as processes, threads, virtual memory, caching, etc.),</li><li>Teach students to use modern operating system calls such as Linux process and synchronization libraries.</li><li>Develop a sense in understand designing and implementing systems and working as part of a team.<br><br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">A. Knowledge and understanding</span></strong><br></p><p>After completing this module, students will be able to:</p><ol><li>&nbsp;Identify and learn what operating systems are, what they do.</li><li>Describe How the Operating System are designed and constructed.</li><li>&nbsp;Show what the common features of an operating system are. </li><li>Explain what an operating system does for the user, and what it does&nbsp;&nbsp; for the computer-system operator.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">B. Cognitive skills</span></strong><br></p><p>After completing this module, students will be able to:</p><ol><li>Analyze the operating system design, constructor, building, internal&nbsp;&nbsp; works, usage variety, operations, and functions.</li><li>&nbsp;Demonstrate the basis for future work in other areas of OS: hacking Linux, i.e. contribute to the Open source OS, security and so on&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">C. Practical and professional skills</span></strong><br></p><p>After completing this module, students will be able to:</p><ol><li>Implement the design simple of Operating System structures.</li><li>Demonstrate basic skills to enable you to progress to more advanced level studies at the AOU or any other university.&ZeroWidthSpace;</li></ol><p><strong><span lang="EN-GB" style="font-size:12pt;font-family:&quot;times new roman&quot;, serif;">D. Key transferable skills&nbsp;</span></strong><br></p><p>After completing this module, students will be able to:</p><ol><li>Demonstrate study skills at a level appropriate to higher education, such as timetabling study; read critically for meaning and take effective notes; and use study aids such as dictionaries and glossaries;</li><li>Identify and distinguish between number of concepts that inform the Operating system structure components.</li><li>&nbsp;Communicate appropriately with your tutor and other students using email, online conferences and forums;</li><li>&nbsp;Locate information on a given subject from the World Wide Web.&ZeroWidthSpace;<br><br></li></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM351&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Data management and analysis <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Data management and analysis (TM351) – an overview of the concepts, techniques, and tools of modern data management and analysis. The requirements of data management continually evolve.  Recently those requirements have surpassed the capabilities of traditional data management.  So, in order to better prepare our graduates for the new demands of the job market, it is necessary to address both the traditional concepts of data management as well as the increasingly important area of data analytics.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_24">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_24" class="modal fade" role="dialog" style="display: none;" aria-hidden="true">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Data management and analysis</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM351</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Data management and analysis</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Data management and analysis (TM351) – an overview of the concepts, techniques, and tools of modern data management and analysis. The requirements of data management continually evolve.  Recently those requirements have surpassed the capabilities of traditional data management.  So, in order to better prepare our graduates for the new demands of the job market, it is necessary to address both the traditional concepts of data management as well as the increasingly important area of data analytics.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;<span class="ms-rteThemeFontFace-1" style="font-size:13px;">This module aims to address some of the key concepts required for the traditionally important area of data management, and the increasingly important area of data analytics. The module will compare traditional relational databases with an alternate model (a NoSQL database), and will enable students to choose between the alternatives to select an appropriate means of storing and managing data, depending on the size and structure of a particular dataset and the use to which that data will be put. Students will be introduced to preliminary techniques in data analysis, starting from the position that data is used to answer a question, and introduced to a range of data visualisation and visual analysis techniques that will instil an understanding of how to start exploring a new data set.</span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">To ensure that students are comfortable with handling datasets, they will explore a range of openly licensed real-world datasets (either downloaded from their host websites, or provided as snapshots) to illustrate the key concepts in the course. Sources such as data.gov.uk, the World Bank, and a range of other national and international agencies will be used to provide appropriate data.&nbsp; The module will aim to divide approximately equally between issues in data management (technical and socio-legal issues in storing and maintaining datasets), and issues in data analytics (using data to answer questions). Students are not expected to have a background in statistics, but should be comfortable working with mathematical concepts and will need to be competent programmers.</span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">The module will be framed around a narrative that looks at how to manage and extract value and insight from a range of increasingly large data collections. At each stage, a comparison will be drawn between different ways of representing the data (for example, using different sorts of charts or geographical mapping techniques), and limitations of the mechanisms presented. To enable students to get a feel for the use of data, each stage will also include an overview of some data analysis techniques, including summary reporting and exploratory data visualisation. The module will be driven by Richard Hamming's famous quote: The purpose of computing is insight, not numbers.</span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Some of the key ideas are:</span></p><ul><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Introducing data analysis. Starting with a text based data file such as comma separated variable (CSV) document, this unit will provide a brief introduction to some basic operations on simple data files. This will give an opportunity to provide an outline of the key ideas in the module, to ensure that the students have installed the module software correctly, and to begin to familiarise themselves with that software.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Concepts in data management. The module will look at three key areas in data management: data architectures and data access (CRUD), data integrity, and transaction management (ACID). Each of these will be illustrated using a relational database, and one non-relational alternative, and the advantages and limitations of each model discussed.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Legal and ethical issues. The module will consider the legal and ethical issues involved in managing data collections. Students will be required to obtain and read (parts of) the Data Protection Act and the Freedom of Information Act, and demonstrate how these apply to issues in data management. They will also consider privacy, ownership, intellectual property and licensing issues in data collection, management, retrieval and reuse.</span></li></span></ul><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Concepts in data analytics. These sections will focus on using data to answer a real question; the focus will be on exploratory techniques (such as visualisation) and formulating a question into a form which can realistically be answered using the data that is available. Issues in processing techniques for large and real-time streamed data collections will also be addressed along with techniques and technologies (such as mapreduce) for handling them. This part will use a statistical package such as the python scientific libraries and/or ggplot to visualise the data and carry out appropriate analyses. It is not anticipated that students will need to understand statistical methods in depth.&ZeroWidthSpace;<br></span></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Discuss and describe the similarities and differences between at least two different database models, and how they are used to manage data collections.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Identify and explain the legal issues surrounding data collection, usage and retention.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Explain the stages and process of database design&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">B. Cognitive skills</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Select an appropriate database model for a data collection.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use data to answer a practical question.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Analyse a simple scenario to produce a conceptual model.&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use a query language to extract information from a database.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use a statistical package to explore a data set</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Present an analysis of a dataset to a variety of audiences.&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Write a report detailing a systematic approach to analysing a data set.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Gain Active listening to the stakeholders regarding their data analysis needs</span></li></span></ol><p><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Communicate the results of data analysis to stakeholders at appropriate level</span><br></span></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM352 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Web, mobile and cloud technologies <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Cloud computing and mobile technologies offer new possibilities for the production and distribution of IT applications and services. Rapid, elastic and scalable provisioning of IT resources allows organisations to be more innovative, agile and cost effective. In our personal lives, cloud and mobile technologies allow us to store, access and share information online. Storing and processing information with no clear physical location or legal authority raises important concerns around governance and security. In this module students will learn about the technical and social aspects of cloud computing and mobile technologies, and they will gain hands-on experience of these technologies.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_25">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_25" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Web, mobile and cloud technologies</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM352 </td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Web, mobile and cloud technologies</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Cloud computing and mobile technologies offer new possibilities for the production and distribution of IT applications and services. Rapid, elastic and scalable provisioning of IT resources allows organisations to be more innovative, agile and cost effective. In our personal lives, cloud and mobile technologies allow us to store, access and share information online. Storing and processing information with no clear physical location or legal authority raises important concerns around governance and security. In this module students will learn about the technical and social aspects of cloud computing and mobile technologies, and they will gain hands-on experience of these technologies.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul><li>Provide knowledge to students about foundations of the internet and the mechanisms of web services and applications provisioning.</li><li>Teach students about the cloud model and the associated resources of a cloud infrastructure.</li><li>Impart knowledge to students about the business case for cloud and the different ways to distributing the cloud infrastructure.</li><li>Create awareness in students concerning the various challenges involved in mobile application development and the combined use of mobile technology and cloud technology.</li><li>Enable students to develop and deploy web services to an application server and perform exploration of toolkits for developing mobile applications.<br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Knowledge and understanding of:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">The different approaches to providing network applications and services including the architectures and protocols involved.<br></span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">The security and legal issues related to the adoption and use of cloud services, data and applications.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">The risks and benefits of adopting cloud and mobile technology for a range of business models.</span></li></span></ol><div><font class="ms-rteThemeFontFace-1" style="font-size:13px;"><b><strong><span lang="EN-GB">B. Cognitive skills</span></strong><br></b></font></div><div><font class="ms-rteThemeFontFace-1" style="font-size:13px;"><b><strong><span lang="EN-GB"><br></span></strong></b></font></div><div><span style="font-size:13px;"><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this module, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Analyse and critique an organisation's approach to IT infrastructure and delivery of applications and services.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Design an effective approach to IT infrastructure for an organisation utilising cloud technology appropriately.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Create prototypes of cloud services and mobile applications.<br></span></li></span></ol><font class="ms-rteThemeFontFace-1" style="font-size:13px;"><b><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></b></font></span></div><div><font class="ms-rteThemeFontFace-1" style="font-size:13px;"><b><strong><span lang="EN-GB"><br></span></strong></b></font></div><div><span style="font-size:13px;"><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this module, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Implement IT solutions to address legal, ethical and security issues related to cloud based resources and access to data, applications and services.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Deploy, demonstrate and utilise a cloud infrastructure</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Create a mobile application and adapt this to utilise cloud based resources.<br></span></li></span></ol><font class="ms-rteThemeFontFace-1" style="font-size:13px;"><b><strong><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong><br></b></font></span></div><div><font class="ms-rteThemeFontFace-1" style="font-size:13px;"><b><strong><span lang="EN-GB"><br></span></strong></b></font></div><div><span style="font-size:13px;"><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this module, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Research and analyse an organisation's IT infrastructure and identify opportunities for cloud technology adoption.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Plan and produce a structured technical report detailing an approach for an organisation which is adopting cloud and mobile technologies.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;Produce a presentation to convey the means, risks and benefits for an organisation to adopt cloud and mobile technologies&ZeroWidthSpace;</span></li></span></ol></span></div></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM354&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Software Engineering <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Software engineering (TM354) – the intellectual tools needed to design, build, and test software systems. This module aims to provide you with an understanding of software engineering concepts and a view of practical software development. It follows a disciplined approach to the development of software systems to meet specified requirements. You will become familiar with a wide range of techniques to support the dialogue between software engineers and an organisation’s stakeholders, and the work of the developers. You will also develop a good understanding of the different approaches to, and practices of, software development, including those followed by agile methods.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_26">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_26" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Software Engineering</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM354</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Software Engineering</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Software engineering (TM354) – the intellectual tools needed to design, build, and test software systems. This module aims to provide you with an understanding of software engineering concepts and a view of practical software development. It follows a disciplined approach to the development of software systems to meet specified requirements. You will become familiar with a wide range of techniques to support the dialogue between software engineers and an organisation’s stakeholders, and the work of the developers. You will also develop a good understanding of the different approaches to, and practices of, software development, including those followed by agile methods.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul><li>&ZeroWidthSpace;To understand the business domain for a problem requiring a software solution or a change to an existing solution</li><li>To acquire the tools and knowledge to analyse and design such a solution or change</li><li>To understand how any chosen software architecture will impact on the satisfaction of all users requirements and expectations</li><li>To apply and reuse design expertise from a set of design patterns</li><li>To develop the skills for testing outputs of all activities throughout the development process.&ZeroWidthSpace;<br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><p style="text-align:justify;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this module, students will be able to:<br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Understand concepts of software development and maintenance, specialising in such topics as Web and Internet design and programming, advanced database techniques or human computer interaction</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Acquire the methods and tools used to develop a range of software systems</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Identify a range of situations in which computer systems are used, the ways in which people interact with them, and the ethical, social and legal problems that computer software can create.<br></span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">B. Cognitive skills</span></strong><br></span></p><p style="text-align:justify;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this module, students will be able to:</span></p><p style="text-align:justify;">&nbsp;</p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Explain advanced software development concepts and apply them to practical problems, including in an extended piece of work</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Analyse problems, and design and evaluate realistic solutions to them</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Compare and contrast a variety of computing methods and tools, identifying the best choices to apply to specific problems</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Explain the various roles, functions and interactions of members of a software development team.<br></span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></p><p style="text-align:justify;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this module, students will be able to:<br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Work independently, planning, monitoring, reflecting on and improving your own learning and working practices</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Work in a group, communicating computing ideas effectively in speech and in writing</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Find, assess and apply information from a variety of sources, using information technology where necessary, in a number of assignments, including at least one significant piece of work</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use numerical and analytical techniques confidently to solve complex problems.</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong><br></span></p><p style="text-align:justify;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this module, students will be able to:<br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Design, program, test and evaluate software systems</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&nbsp;Use modern software tools, both within and outside your workplace</span></li><li><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Identify and handle the ethical, social and legal issues that may arise during software development and use.&ZeroWidthSpace;&ZeroWidthSpace;</span><br><br></span></li></span></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM355&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Communications Technology <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Communications technology (TM355) – looks at the underlying technologies of modern electronic communications, such as mobile data and telephony, broadband, Wi-Fi, and optical fiber. Electronic communication is ubiquitous in homes, offices and urban environments. This module gives students an insight into these and other questions, by looking at the fundamental principles of communications technologies. Through these principles students will gain an insight into the possibilities and constraints of modern communications technology. This module complements other modules relating to networking (e.g., T215A/B, T216A/B and T316). 
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_27">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_27" class="modal fade" role="dialog" style="display: none;" aria-hidden="true">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Communications Technology</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM355</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Communications Technology</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Communications technology (TM355) – looks at the underlying technologies of modern electronic communications, such as mobile data and telephony, broadband, Wi-Fi, and optical fiber. Electronic communication is ubiquitous in homes, offices and urban environments. This module gives students an insight into these and other questions, by looking at the fundamental principles of communications technologies. Through these principles students will gain an insight into the possibilities and constraints of modern communications technology. This module complements other modules relating to networking (e.g., T215A/B, T216A/B and T316). </td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;TM355 is framed fairly precisely by its areas of interest: layers 1 and 2 of the OSI seven-layer model, that is the Physical Layer (layer 1) and the Data Link Layer (layer 2); and the three access technologies of optical fibre, DSL broadband and wireless.</span></p><p><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Within this framing, TM355 is concerned to reveal and explore commonalities that cut across these technologies, such as Shannon's law, multiple access (which increasingly means orthogonal frequency division multiple access, or OFDMA), modulation techniques (in the digital world, almost synonymous with quadrature amplitude modulation, or QAM), error detection and correction, and coding. A thorough understanding of the principles of these common technologies will equip students to understand a range of communication technologies, and to understand their potential and limitations</span><br></span></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;<strong><span lang="EN-GB" style="color:black;">A. Knowledge and
understanding</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Have a sound grasp of the essential vocabulary of communications technology, be able to deploy it appropriately, and be able to explain them</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Understand the main principles and constraints of digital communications technology at the physical and data link layers, and employ them to analyse and assess communication scenarios.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Understand the essential limits and trade-offs that are inherent in practical communication systems&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB" style="color:black;">B. Cognitive skills</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use relevant data related to a communication system to model its behaviour and assess performance and resource requirements.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Explain how and why particular communications configurations and systems are used, discuss their potential and limitations.<br></span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB" style="color:black;">C. Practical and
professional skills</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Write a short report or essay discussing applications of communications technology.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Be able to use third-party material critically.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Be able to incorporate copyrighted material appropriately&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB" style="color:black;">D Key transferable skills&nbsp;</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Assess and synthesise information from a range of sources in order to offer an informed judgement on applications of communication technology.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Develop your own learning skills in topics related to communications technology.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;Be able to learn independently from third-party materials, in order to keep up to date in communications technology.&ZeroWidthSpace;&ZeroWidthSpace;</span></li></span></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM356 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Interaction design and user experience <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Interaction design and the user experience (TM356) – in this module the students will learn the importance of user-centred design, and acquire practical skills for designing the interactive products for everyday life.
From apps, phones and business systems to wearables, the web and the Internet of Things, interactive products are the stuff of everyday life. But how can interactions be designed to best meet their purposes, offer good user experiences, and be easy, satisfying and enjoyable to use? How can interactions be evaluated effectively when their users, purposes and contexts of use vary so widely? In this module we take a user-centred approach through which the student will learn about the factors, techniques, tools and theories that affect interaction design and acquire practical skills that will equip the student to analyse, design, and evaluate the interactive products of everyday life. Why are some interactive products so popular? How do you create products that everybody wants? One of the fundamental things the student will learn in this module is the importance of user-centred design. In this context, this module complements the rest of Web Development modules.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_28">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_28" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title"> Interaction design and user experience</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM356 </td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td> Interaction design and user experience</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Interaction design and the user experience (TM356) – in this module the students will learn the importance of user-centred design, and acquire practical skills for designing the interactive products for everyday life.
From apps, phones and business systems to wearables, the web and the Internet of Things, interactive products are the stuff of everyday life. But how can interactions be designed to best meet their purposes, offer good user experiences, and be easy, satisfying and enjoyable to use? How can interactions be evaluated effectively when their users, purposes and contexts of use vary so widely? In this module we take a user-centred approach through which the student will learn about the factors, techniques, tools and theories that affect interaction design and acquire practical skills that will equip the student to analyse, design, and evaluate the interactive products of everyday life. Why are some interactive products so popular? How do you create products that everybody wants? One of the fundamental things the student will learn in this module is the importance of user-centred design. In this context, this module complements the rest of Web Development modules.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;The student will learn the value of moving away from his/her desk and 'stepping out into the world' to involve potential users in his/her early design ideas for interactive products. It is all too easy to assume that other people think, feel and behave in the same way as the designer or developer, do. It is essential to take into account the diversity among users and their different perspectives and getting their feedback will help to avoid any errors and misunderstandings that may not have thought of. Involving users in the process is vital to creating great products and makes good business sense.</span></p><p><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Through hands-on activities the student will work through the design process on a topic chosen by himself/herself (with tutor's guidance). The student will develop skills that will be important to him/her in a variety of employment settings – whether working as a developer as part of a large software development team, as a partner in a small start-up, or in some other role involved in the managing of, or decision making around interactive products that will be used by people</span><br></span></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After studying the module students will have knowledge and understanding of:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">What interaction design is about and the importance of user centred design and methods that take into account activities and tasks, context of use and user experiences; </span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&nbsp;The sensory, cognitive and physical capabilities of users and how these inform the design of interactive products;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&nbsp;The process of interaction design including requirements elicitation, prototyping, evaluation and the need for iteration.<br></span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">B. Cognitive skills</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After studying the module students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&nbsp;Analyse and critique the design of interactive products;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&nbsp;Select, adapt and apply suitable interaction design approaches and techniques towards the design of an interactive product;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&nbsp;Construct prototypes for diverse purposes using appropriate materials or tools;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&nbsp;Analyse and critique how interaction design activities have been conducted.&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After studying the module students will be able to:</span></p><ol><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Define a suitable programme of user involvement that treats users ethically and fairly.<br></span></li></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After studying the module students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&nbsp;Construct and convey an argument from a variety of sources to persuade a non-specialist audience of the importance of user-centred design when designing interactive products;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&nbsp;Communicate effectively about requirements, design, and evaluation activities relating to interactive products;</span></li><li><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;&nbsp;To progress your own learning independently using materials and publications from a wide variety of sources</span>.&ZeroWidthSpace;<br></span></li></span></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM366&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Artificial intelligence <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Basic concepts in artificial intelligence are being used in huge research projects all over the world for the last three decades. This includes research and development at the industrial and academic levels. The module introduces the students to the basics natural intelligence where AI has been inspired and presents the AI concepts and techniques that are being used in advanced AI projects. 
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_29">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_29" class="modal fade" role="dialog" style="display: none;" aria-hidden="true">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Artificial intelligence</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM366</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Artificial intelligence</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Basic concepts in artificial intelligence are being used in huge research projects all over the world for the last three decades. This includes research and development at the industrial and academic levels. The module introduces the students to the basics natural intelligence where AI has been inspired and presents the AI concepts and techniques that are being used in advanced AI projects. </td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;T</span><span class="ms-rteThemeFontFace-1" style="font-size:13px;">o provide the students
with an understanding of the fundamental concepts involved in natural and
artificial intelligence (ASO, PSO, neural networks, evolutionary computing,
robotics and genetic computing).</span><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;</span><br></span></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completion of this module the student will gain knowledge and &nbsp;understanding of: </span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">The aims of, and motivations for, artificial intelligence;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">The principal techniques used in traditional approaches to artificial intelligence, i.e. knowledge representation and search;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">The four key principles of nouvelle AI: interaction, emergence, adaptation and selection;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">The biological basis of modern techniques in AI;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Key concepts and methods in artificial neural networks;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Key concepts and methods in evolutionary computation.&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">B. Cognitive skills</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completion of this module the student will be able to: </span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Analyse a problem in terms of its amenability to solution by various computational methods;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Formulate computational solutions to diverse problems;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Select and use appropriate mathematical representations for a range of problem solving systems;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Compare, contrast and evaluate competing approaches to computational problem solving and the simulation of intelligence;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Synthesise the main concepts of the module into a clear and critical view of the strengths, weaknesses and future direction of AI.&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completion of this module the student will be able to:<span style="text-decoration:underline;"><strong> </strong></span></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Analyse, design and evaluate computer simulations;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Construct computer systems using an appropriate tool;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Carry out experiments, with careful recording, analysis and evaluation of results;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use basic research techniques&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completion of this module the student will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Apply appropriate computational problem-solving techniques to a range of problems;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Communicate computational ideas relating to AI in clear and concise written English;</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use appropriate graphical, logical and mathematical representations to characterize various types of AI system;</span></li><li><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Exercise general numeracy and problem-solving skills</span>.&ZeroWidthSpace;&ZeroWidthSpace;<br><br></span></li></span></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM391&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E-Commerce <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Technologies of the Internet are essential for conducting businesses in this information age and this module is meant to provide the foundations for e-Commerce Technologies, help in selecting appropriate technology infrastructure and security measures.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_48">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_48" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">E-Commerce</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM391</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>E-Commerce</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Technologies of the Internet are essential for conducting businesses in this information age and this module is meant to provide the foundations for e-Commerce Technologies, help in selecting appropriate technology infrastructure and security measures.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;The module aims to provide an understanding of e-business and its associated technologies. The basics of online commerce will be introduced along with the elements that are particular to an electronic marketplace.<br></p><p>The module aims to provide students with:</p><ol><li>An understanding and the nature of e-Commerce, recognize the business impact and potential of e-Commerce.</li><li>Basic understanding of internet technologies and network infrastructure.</li><li>Major business and revenue models and how to do marketing online, communicating with different market segments.</li><li>Strategies that business uses to improve purchasing, logistics and other support activities, including how Electronic Data Interchange (EDI) works.</li><li>Understanding key characteristics of different major auction types, strategies for web auction sites and auction-related businesses.</li><li>Web server basics, software for web servers and web server hardware.</li><li>Finding and evaluating web hosting services, basic and advance functions of e-commerce software.</li><li>Online security issues, security for communication channels between computers, networks and major servers offering web and e-commerce services.</li><li>The basic function of online payment systems, the use of payment cards in electronic commerce. History and function of electronic cash, including electronic wallets and other internet payment technologies and the banking industry.&ZeroWidthSpace;</li></ol><p><br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong><br></p><p>On completion of the module students will be able to:<br></p><ol><li>Discuss the relationships between e-business and technological developments on the Internet, familiarity with e-business models, B2B, B2C, C2C, comprehend Supply-Chain and Value-Chain concepts.</li><li>Describe a set of e-business models, relationships and strategic issues that arise from the deployment of e-business systems </li><li>Describe various revenue models and how to market on the web, and what e-marketers are doing in the real world.</li><li>Describe the function of protocols and standards used in data exchange</li><li>Describe various auction models; perform virtual communications and interacting with web portals.</li><li>Describe the use of HTML, XML, syntax, properties and processing of XML documents, DTDs and schemas</li><li>Describe the architecture, operation, standards, protocols, and technologies used in the construction, discovery, and use of web services.</li><li>Describe the key dimension of e-commerce security.</li><li>Describe the features of e-commerce payment systems in use.<br></li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">B. Cognitive skills</span></strong><br></p><p>On completion of the module students will be able to:<br></p><ol><li>Relate the business with the technology opportunities and challenges afforded by e-business.</li><li>Critically evaluate an e-business strategy using a suitable framework, appropriate models and current terminology.</li><li>Construct a sound argument that makes use of an appropriate vocabulary with critical use of relevant supporting references.</li><li>Analyse design, develop, implement and manage secure e-commerce systems using a range of tools and techniques, across a range of business contexts to meet various stakeholders requirements.</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></p><p>On completion of the module students will be able to:<br></p><ol><li>Utilize the key protocols of the Internet (especially http, ftp and email), create and edit, HTML XML documents, basics of scripting languages such as PHP, able to create web based data driven applications.</li><li>Choose hardware and software, required for setting up e-commerce business.</li><li>Apply the various e-commerce models and on-line marketing, including auctions and web selling.</li><li>Compare the various on-line payment systems.</li><li>Utilize the various security mechanisms to protect e-commerce systems.<br></li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">D. Key transferable skills&nbsp;</span></strong><br></p><p>On completion of the module students will be able to:<br></p><ol><li>Plan, monitor and evaluate own learning and seek ways to improve the performance.</li><li>Develop secure, flexible, information and communication architectures that support the changing needs of the business.</li><li>Evaluate, and use information or data accurately in complex contexts.&ZeroWidthSpace;<br></li></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM471&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Telematics project CS <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The objective of this module is to provide the students with the opportunity to apply the theoretical and the practical concepts they have learnt during the lower level courses to a real and tangible project. During their last year, students are required in this module to submit a project proposal consistent with the computer science track. They need to use the skills they have acquired in order to accomplish their presumptive proposal.  Beside the deliverable and the assessments, each student has to submit a report that sums up the plan-do-review cycle of his/her work and has to present the findings in front of a faculty committee. 
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_30">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_30" class="modal fade" role="dialog" style="display: none;" aria-hidden="true">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">The Telematics project CS</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM471</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>The Telematics project CS</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>The objective of this module is to provide the students with the opportunity to apply the theoretical and the practical concepts they have learnt during the lower level courses to a real and tangible project. During their last year, students are required in this module to submit a project proposal consistent with the computer science track. They need to use the skills they have acquired in order to accomplish their presumptive proposal.  Beside the deliverable and the assessments, each student has to submit a report that sums up the plan-do-review cycle of his/her work and has to present the findings in front of a faculty committee. </td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;On successful completion of this course, students will be able to:</p><ul><li>Undertake practical projects to solve problems in the area of ITC.</li><li>Perform literature search on a selected topic of interest.</li><li>Apply what they have learnt to plan a project and develop a deliverable.</li><li>Produce project plans for successful undertaking of practical projects.</li><li>Write a detailed project report and communicate their ideas clearly.</li><li>Present their ideas and work formatively before an audience while progressing in their project.</li><li>Present their findings, outcome and deliverable before an audience&ZeroWidthSpace;<br><br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Demonstrate understanding of the fundamental technical concepts and principles relevant to their project</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Apply a systematic approach towards the practical implementation of their project</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Plan a project while preparing a detailed schedule of the project tasks and milestones for 8 months.<br></span></li></span></ol><p><strong class="ms-rteThemeFontFace-1" style="font-size:13px;"><span lang="EN-GB"><strong><span lang="EN-GB">B. Cognitive skills</span></strong><br></span></strong></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Identify and refine the goals and content of their project</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Identify, list and justify the resources, skills and activities needed to carry out the project successfully</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Conduct a proper literature search. Gather, analyse and evaluate relevant information to complete the project successfully</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Critically review how they have tackled the project<br></span></li></span></ol><p><strong class="ms-rteThemeFontFace-1" style="font-size:13px;"><span lang="EN-GB"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></strong></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:<br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Plan and organize their project work appropriately, and keep systematic records of plans, progress and outcomes</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Identify and address the ethical, social and legal issues that may arise during the development and use of Computing and IT systems</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Analyse a practical problem and devise and implement a solution building on the knowledge and skills developed throughout their earlier OU studies and experience.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Provide a tangible solution by accomplishing their deliverable according to their project requirements.</span></li></span></ol><p><strong class="ms-rteThemeFontFace-1" style="font-size:13px;"><span lang="EN-GB"><strong><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong><br></span></strong></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Make effective use of a variety of information sources,&nbsp;including the internet, e-library and demonstrating awareness of the credibility of the source</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Communicate information, ideas, problems and solutions clearly</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Learn independently and reflect on what has been done, with a view to improving skills and knowledge</span></li><li><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;Present their work in a professional manner while addressing the audience in the domain.&ZeroWidthSpace;</span><br></span></li></span></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM471&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Telematics project CwB <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    TM471 is a final year projects course. Students are expected to select topics of their projects consistent with their track that is, directly related to the computing with business track, and also, make use of the skills they have learnt throughout their studies in lower level modules to plan a project, develop it and submit a report on completion of the project. They are expected to do a presentation and perform a working demonstration of their selected project.  
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_31">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_31" class="modal fade" role="dialog" style="display: none;" aria-hidden="true">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">The Telematics project CwB</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM471</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>The Telematics project CwB</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>TM471 is a final year projects course. Students are expected to select topics of their projects consistent with their track that is, directly related to the computing with business track, and also, make use of the skills they have learnt throughout their studies in lower level modules to plan a project, develop it and submit a report on completion of the project. They are expected to do a presentation and perform a working demonstration of their selected project.  </td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;On successful completion of this course, students will be able to:<br></p><ol><li>Undertake practical computing projects to solve problems in the area of business.</li><li>Perform literature search on a selected topic of interest.</li><li>Apply what they have learnt to plan a project and develop a deliverable.</li><li>Produce project plans for successful undertaking of practical projects.</li><li>Write a detailed project report and communicate their ideas clearly.</li><li>Present their ideas and work formatively before an audience while progressing in their project.</li><li>Present their findings, outcome and deliverable before an audience<br><br></li></ol></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">A. Knowledge and understanding</span></strong>&ZeroWidthSpace;<br></p><p>Upon completing this course, students will be able to:</p><ol><li>Demonstrate understanding of the fundamental technical concepts and principles relevant to their project</li><li>Apply a systematic approach towards the practical implementation of their project</li><li>Plan a project while preparing a detailed schedule of the project tasks and milestones for 8 months.<br></li></ol><p><strong>B. Cognitive skills</strong><br></p><p>Upon completing this course, students will be able to:</p><ol><li>Identify and refine the goals and content of their project</li><li>Identify, list and justify the resources, skills and activities needed to carry out the project successfully</li><li>Conduct a proper literature search. Gather, analyse and evaluate relevant information to complete the project successfully</li><li>Critically review how they have tackled the project<br></li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></p><p>Upon completing this course, students will be able to:<br></p><ol><li>Plan and organize their project work appropriately, and keep systematic records of plans, progress and outcomes</li><li>Identify and address the ethical, social and legal issues that may arise during the development and use of Computing and IT systems</li><li>Analyse a practical problem and devise and implement a solution building on the knowledge and skills developed throughout their earlier OU studies and experience.</li><li>Provide a tangible solution by accomplishing their deliverable according to their project requirements.</li></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;">D. Key transferable skills</span></strong>&ZeroWidthSpace;<br></p><p>Upon completing this course, students will be able to:</p><ol><li>Make effective use of a variety of information sources,&nbsp;including the internet, e-library and demonstrating awareness of the credibility of the source</li><li>Communicate information, ideas, problems and solutions clearly</li><li>Learn independently and reflect on what has been done, with a view to improving skills and knowledge</li><li>Present their work in a professional manner while addressing the audience in the domain&ZeroWidthSpace;</li></ol><p><br></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM471&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The Telematics project ITC <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    TM471 is a final year projects course. Students are expected to select topics of their projects consistent with their track that is, directly related to the information technology and computing track, and also, make use of the skills they have learnt throughout their studies in lower level modules to plan a project, develop it and submit a report on completion of the project. They are expected to do a presentation and perform a working demonstration of their selected project.  
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_32">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_32" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title"> The Telematics project ITC</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM471</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td> The Telematics project ITC</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>TM471 is a final year projects course. Students are expected to select topics of their projects consistent with their track that is, directly related to the information technology and computing track, and also, make use of the skills they have learnt throughout their studies in lower level modules to plan a project, develop it and submit a report on completion of the project. They are expected to do a presentation and perform a working demonstration of their selected project.  </td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;On successful completion of this course, students will be able to:</span></p><ul><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Undertake practical projects to solve problems in the area of ITC.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Perform literature search on a selected topic of interest.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Apply what they have learnt to plan a project and develop a deliverable.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Produce project plans for successful undertaking of practical projects.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Write a detailed project report and communicate their ideas clearly.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Present their ideas and work formatively before an audience while progressing in their project.</span></li><li><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Present their findings, outcome and deliverable before an audience</span><br></span></li></span></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;<strong>A. Knowledge and understanding&ZeroWidthSpace;</strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Demonstrate understanding of the fundamental technical concepts and principles relevant to their project</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Apply a systematic approach towards the practical implementation of their project</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Plan a project while preparing a detailed schedule of the project tasks and milestones for 8 months.<br></span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>B. Cognitive skills</strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Identify and refine the goals and content of their project</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Identify, list and justify the resources, skills and activities needed to carry out the project successfully</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Conduct a proper literature search. Gather, analyse and evaluate relevant information to complete the project successfully</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Critically review how they have tackled the project<br></span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:<br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Plan and organize their project work appropriately, and keep systematic records of plans, progress and outcomes</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Identify and address the ethical, social and legal issues that may arise during the development and use of Computing and IT systems</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Analyse a practical problem and devise and implement a solution building on the knowledge and skills developed throughout their earlier OU studies and experience.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Provide a tangible solution by accomplishing their deliverable according to their project requirements.</span></li></span></ol><p><strong class="ms-rteThemeFontFace-1" style="font-size:13px;"><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong></p><p><strong class="ms-rteThemeFontFace-1" style="font-size:13px;"><span lang="EN-GB"></span></strong></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Make effective use of a variety of information sources,&nbsp;including the internet, e-library and demonstrating awareness of the credibility of the source</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Communicate information, ideas, problems and solutions clearly</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Learn independently and reflect on what has been done, with a view to improving skills and knowledge</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;Present their work in a professional manner while addressing the audience in the domain.&ZeroWidthSpace;</span></li></span></ol><p><br></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM471&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Telematics project NS <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Networking track students need to develop projects where they can integrate what they have seen throughout their study in lower level module in on project. This can be achieved through the TM471 module where practical proposals are to be developed during two semesters that solve or at least simulate real life networking projects. The module is assessed through formative assessments where supervisors provide their students with feedback on their progress, and, through formative assessments where the students have to defend their finding in front of a faculty committee where the presentation skills and the project deliverable are evaluated. The students are required as well to provide a scientific project report.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_33">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_33" class="modal fade" role="dialog" style="display: none;" aria-hidden="true">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">The Telematics project NS</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM471</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>The Telematics project NS</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Networking track students need to develop projects where they can integrate what they have seen throughout their study in lower level module in on project. This can be achieved through the TM471 module where practical proposals are to be developed during two semesters that solve or at least simulate real life networking projects. The module is assessed through formative assessments where supervisors provide their students with feedback on their progress, and, through formative assessments where the students have to defend their finding in front of a faculty committee where the presentation skills and the project deliverable are evaluated. The students are required as well to provide a scientific project report.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;&ZeroWidthSpace;On successful completion of this course, students will be able to:</span></p><ul><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Undertake practical projects to solve problems in the area of ITC.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Perform literature search on a selected topic of interest.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Apply what they have learnt to plan a project and develop a deliverable.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Produce project plans for successful undertaking of practical projects.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Write a detailed project report and communicate their ideas clearly.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Present their ideas and work formatively before an audience while progressing in their project.</span></li><li><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Present their findings, outcome and deliverable before an audience</span><br></span></li></span></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span style="font-size:13px;">&ZeroWidthSpace;<strong>A. Knowledge and understanding</strong><br></span></p><p>Upon completing this course, students will be able to:</p><ol><span style="font-size:13px;"><li>demonstrate understanding of the fundamental technical concepts and principles relevant to their project</li><li>Students should be able to apply a systematic approach towards the practical implementation of their project</li><li>Students should be able to plan a project while preparing a detailed schedule of the project tasks and milestones for 8 months.<br></li></span></ol><div><span style="font-size:13px;"><strong><span lang="EN-GB" style="font-family:arial, sans-serif;">B. Cognitive skills</span></strong><br></span></div><p>&nbsp;</p><p>Upon completing this course, students will be able to:</p><ol><span style="font-size:13px;"><li>Identify and refine the goals and content of their project</li><li>Identify, list and justify the resources, skills and activities needed to carry out the project successfully</li><li>Conduct a proper literature search. Gather, analyse and evaluate relevant information to complete the project successfully</li><li>Critically review how they have tackled the project<br></li></span></ol><p><span style="font-size:13px;"><strong><span lang="EN-GB" style="font-family:arial, sans-serif;">C. Practical and professional skills</span></strong><br></span></p><p>Upon completing this course, students will be able to:</p><ol><span style="font-size:13px;"><li>Plan and organize their project work appropriately, and keep systematic records of plans, progress and outcomes</li><li>Identify and address the ethical, social and legal issues that may arise during the development and use of Computing and IT systems</li><li>Analyse a practical problem and devise and implement a solution building on the knowledge and skills developed throughout their earlier OU studies and experience.</li><li>Provide a tangible solution by accomplishing their deliverable according to their project requirements.</li></span></ol><p><span style="font-size:13px;"><strong><span lang="EN-GB" style="font-family:arial, sans-serif;">D. Key transferable skills&nbsp;</span></strong><br></span></p><p>Upon completing this course, students will be able to:</p><ol><span style="font-size:13px;"><li>Make effective use of a variety of information sources,&nbsp;including the internet, e-library and demonstrating awareness of the credibility of the source</li><li>Communicate information, ideas, problems and solutions clearly</li><li>Learn independently and reflect on what has been done, with a view to improving skills and knowledge</li><li>Present their work in a professional manner while addressing the audience in the domain.&ZeroWidthSpace;<br></li></span></ol><p><strong><span lang="EN-GB" style="font-size:11pt;font-family:arial, sans-serif;"><br></span></strong></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TM471&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Telematics project WD <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    In this module, students will have the opportunity to develop a project and learn to produce the professional documentation accompanying any project implementation. Focusing on web development, this module will help students to be more prepared for the market, because, they are required to plan and implement a web development project that is, at the same level, or higher, than the web systems based on latest web development techniques. Students work is assessed through tutor marked assessments where continuous feedback is provided from the students’ supervisor, and, the final product will be judged by a faculty committee. Students are required to work on their project presentation skill as well, because, this skill will be evaluated by the faculty committee as well during the project defense.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_34">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_34" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">The Telematics project WD</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TM471</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>The Telematics project WD</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>In this module, students will have the opportunity to develop a project and learn to produce the professional documentation accompanying any project implementation. Focusing on web development, this module will help students to be more prepared for the market, because, they are required to plan and implement a web development project that is, at the same level, or higher, than the web systems based on latest web development techniques. Students work is assessed through tutor marked assessments where continuous feedback is provided from the students’ supervisor, and, the final product will be judged by a faculty committee. Students are required to work on their project presentation skill as well, because, this skill will be evaluated by the faculty committee as well during the project defense.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;On successful completion of this course, students will be able to:</p><ul><li>Undertake practical projects to solve problems in the area of ITC.</li><li>Perform literature search on a selected topic of interest.</li><li>Apply what they have learnt to plan a project and develop a deliverable.</li><li>Produce project plans for successful undertaking of practical projects.</li><li>Write a detailed project report and communicate their ideas clearly.</li><li>Present their ideas and work formatively before an audience while progressing in their project.</li><li>Present their findings, outcome and deliverable before an audience&ZeroWidthSpace;<br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">demonstrate understanding of the fundamental technical concepts and principles relevant to their project</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Students should be able to apply a systematic approach towards the practical implementation of their project</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Students should be able to plan a project while preparing a detailed schedule of the project tasks and milestones for 8 months.&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>B. Cognitive skills</strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Identify and refine the goals and content of their project</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Identify, list and justify the resources, skills and activities needed to carry out the project successfully</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Conduct a proper literature search. Gather, analyse and evaluate relevant information to complete the project successfully</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Critically review how they have tackled the project</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&nbsp;<strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Plan and organize their project work appropriately, and keep systematic records of plans, progress and outcomes</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Identify and address the ethical, social and legal issues that may arise during the development and use of Computing and IT systems</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Analyse a practical problem and devise and implement a solution building on the knowledge and skills developed throughout their earlier OU studies and experience.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Provide a tangible solution by accomplishing their deliverable according to their project requirements.&ZeroWidthSpace;</span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Upon completing this course, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Make effective use of a variety of information sources,&nbsp;including the internet, e-library and demonstrating awareness of the credibility of the source</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Communicate information, ideas, problems and solutions clearly</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Learn independently and reflect on what has been done, with a view to improving skills and knowledge</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;Present their work in a professional manner while addressing the audience in the domain&ZeroWidthSpace;</span></li></span></ol><p><br></p></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TT284&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Web technologies <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module is meant to introduce students to the foundations of web applications, including protocols, standards and content handling.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_20">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_20" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Web technologies</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TT284</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Web technologies</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module is meant to introduce students to the foundations of web applications, including protocols, standards and content handling.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul><li>give students an insight into architectures, protocols, standards, languages, tools and techniques;</li><li>give students an understanding of approaches to more dynamic and mobile content;&ZeroWidthSpace;<br><br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After completing this module, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Describe how the development of the Web has enabled the creation of new forms of information systems and impacted commerce and public services.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Explain different architectural approaches to application design and contrast traditional approaches with the underlying client–server model of Web applications.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Describe the roles of the range of protocols and standards associated with Web applications and their communications, for the development of web applications.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Explain the operation and properties of service, distributed and mobile approaches to web architecture.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Demonstrate knowledge of a range of different programming languages and explain their differing roles and properties for web applications.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Discuss issues of web design including, accessibility, usability, localisation and globalisation and the nature of static and dynamic content and different content delivery approaches</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Explain a range of security issues including secure protocols, use of certificates, authentication, authorisation, and firewalls&ZeroWidthSpace;</span></li></span></ol><p><strong class="ms-rteThemeFontFace-1" style="font-size:13px;"><span lang="EN-GB"><strong>B. Cognitive skills</strong><br></span></strong></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After completing this module, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Analyse requirements to produce a design for a simple web application, applying an understanding of requirements for aspects such as usability and accessibility.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Describe a suitable architecture, components and standards as the basis for implementation of a web application for a public or business organisation.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Construct, using appropriate code, a simple web application selecting and reusing code etc where appropriate. , transforms content and integrates services to produce a mobile application&ZeroWidthSpace;</span></li></span></ol><p><strong class="ms-rteThemeFontFace-1" style="font-size:13px;"><span lang="EN-GB"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></strong></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After completing this module, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Outline the importance of standards and standardisation bodies.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Maintain an up-to-date view of ongoing developments in web technology including standards and techniques.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Produce and manage design and development plans for a specific technical solution to a challenge in Web application development.&ZeroWidthSpace;</span></li></span></ol><p><strong class="ms-rteThemeFontFace-1" style="font-size:13px;"><span lang="EN-GB"><strong><span lang="EN-GB">D. Key transferable skills&nbsp;</span></strong><br></span></strong></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After completing this module, students will be able to:</span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Find, select and use information from a range of sources to support analysis, design and implementation tasks.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Plan and produce a well-structured and researched quality report as part of a project.</span></li><li><span style="font-size:13px;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;Plan and manage effort and progress whilst undertaking a substantial project.&ZeroWidthSpace;</span><br></span></li></span></ol></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        

            <div class="course-item">
                <div class="course-title">
                    TU170&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Computing Essentials <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This is an introductory course which introduces students to the essential concepts related to computing essentials. This is a fundamental course for all students enrolled in AOU.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_36">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_36" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Computing Essentials</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>TU170</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Computing Essentials</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>-</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This is an introductory course which introduces students to the essential concepts related to computing essentials. This is a fundamental course for all students enrolled in AOU.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul><li>To develop basic skills of “<em>Learning"</em></li><li>To know e-Learning: meaning, accessibility, skills, and resources</li><li>To familiarize with the basic concepts of Information Technology: Internet, Web, and Systems</li><li>To familiarize with basic computer system applications: software and hardware</li><li>To learn some practical skills for using computers</li><li>To introduce the concepts of: Security and Ethics<br><br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1 ms-rteFontSize-3" style="font-size:13px;">&ZeroWidthSpace;<strong><span lang="EN-GB">A. Knowledge and understanding</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After studying the course, the student will be able to:<br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Understand terminologies related to IT and computer</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Understand the different learning styles</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Describe the difference between Conventional and blended-learning education systems</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Understand how to read and take notes in the process of learning</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Describe the social media types and facilities</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Have a background about the Web and Internet inventions</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Understand and explain what is information system and technology</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Know the types of applications</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Describe the e-commerce</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Explain different part in computer system (Hardware such as system unite, input and output, memory and processor)</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Explain different terms in communication such as network, connectivity, wireless, server, client)</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Understand clearly what is the difference between privacy and security)</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Describe what are computer ethics and computer crime&nbsp;<br></span></li></span></ol><div><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>B. Cognitive skills</strong><br><br></span></div><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">After studying the course, the student will be able to:<br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Learn by himself</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Deal with computer problems</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Describe the difference between different learning styles</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Describe the web and search engines<br></span></li></span></ol><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB">C. Practical and professional skills</span></strong><br></span></p><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">To be able to<br></span></p><ol><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Operate the computer system properly</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Interact with applications and programs such as (MS office) confidently</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Communicate with others electronically (Email, instant messaging, blogs, micro-blogs and wikis)</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Read analytically and critically for the purpose of learning </span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Avoid plagiarisms</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Initiate a transaction electronically (e-commerce) in a secure way</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use the social media in the process of learning and communication with others.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Connect and surf the internet</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Search using the search engines.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Send and receive email, and share files in a secure way.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Avoid computer crime</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Use com&ZeroWidthSpace;puter ethically&ZeroWidthSpace;</span></li></span></ol><strong class="ms-rteThemeFontFace-1" style="font-size:13px;">D Key transferable skills&nbsp;</strong><br class="ms-rteThemeFontFace-1" style="font-size:13px;"><div><br class="ms-rteThemeFontFace-1"></div><div><span style="font-size:13px;"><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">To be able to</span></p><ol style="list-style-type:decimal;"><span style="font-size:13px;"><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Interact effectively within a group using social media and electronic conferencing techniques.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Working in groups using the LMS system and course forum online.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Contribute to discussions on a conference using instant messaging.</span></li><li><span class="ms-rteThemeFontFace-1" style="font-size:13px;">Improve own learning and performance</span></li></span></ol><br></span></div></td>
										</tr>
									</tbody>
								</table>
								
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				
				
                
                
            </div>

        
</div>
"""

soup = BeautifulSoup(html_content, "html.parser")

# Create a list to store course details
courses = []

# Find all course items
course_items = soup.find_all("div", class_="course-item")

for item in course_items:
    course = {}

    # Extract course title and code
    title_code = item.find("div", class_="course-title").get_text(strip=True)
    title_parts = title_code.split()
    course_code = title_parts[0]
    course_title = " ".join(title_parts[1:]).split('(')[0].strip()
    course['course_code'] = course_code
    course['course_title'] = course_title

    # Extract credit hours
    credit_hours = item.find("span", class_="float-right").get_text(strip=True).replace("Credit Hours", "").strip("()")
    course['credit_hours'] = credit_hours

    # Extract course description
    course_desc = item.find("div", class_="course-desc").get_text(strip=True)
    course['course_description'] = course_desc

    # Extract modal details if available
    modal = item.find("div", class_="modal-body")
    if modal:
        modal_table = modal.find("table")
        if modal_table:
            rows = modal_table.find_all("tr")
            for row in rows:
                cols = row.find_all("td")
                if len(cols) == 2:
                    key = cols[0].get_text(strip=True).lower().replace(" ", "_")
                    value = cols[1].get_text(strip=True)
                    course[key] = value

    courses.append(course)

# Specify the CSV file name
csv_file = "scrappedCourses.csv"

# Define the header for the CSV
headers = ["course_code", "course_title", "credit_hours", "course_description", "pre-requisite", "course_objectives", "course_outcomes"]

# Write the data to CSV
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for course in courses:
        writer.writerow(course)

print(f"Data has been written to {csv_file}")
