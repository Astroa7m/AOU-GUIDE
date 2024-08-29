import csv

import requests
from bs4 import BeautifulSoup

# Sample HTML
html_content = """
<div id="ctl00_ctl50_g_6ce2bd0e_6228_4092_9c97_2ca3d1f0486e_ctl00_dWebpart" class="wp-wrapper">

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
                    ACC300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Accounting Information Systems <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This course is the first module to introduce the domain of information systems in accounting. This is a Level 6 course and students need to have a good knowledge of financial accounting, obtained through Levels 4 and 5 accounting modules. Thus, it is strongly recommended that students study this course after studying Financial/Management accounting (B291 and B292).
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
								<span class="modal-title">Accounting Information Systems</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>ACC300</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Accounting Information Systems</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B291 and B292</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This course is the first module to introduce the domain of information systems in accounting. This is a Level 6 course and students need to have a good knowledge of financial accounting, obtained through Levels 4 and 5 accounting modules. Thus, it is strongly recommended that students study this course after studying Financial/Management accounting (B291 and B292).</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p style="text-align:justify;">&ZeroWidthSpace;This course is designed to present an understanding of accounting information systems and their role in the accounting environment. Particular attention is paid to transaction cycles and internal control structure. The three broad aims of the course are to provide students with: &nbsp;<br></p><ol><li>an understanding of the purpose and role of accounting information systems within contemporary organisations.&nbsp; </li><li>an awareness of the way in which internal controls and technology interrelate with accounting information systems.</li></ol><p>an understanding of the real-life problems of designing, implementing and using accounting information systems and its sub-cycles.<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>A. Knowledge
and understanding</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1: Explain what an accounting information system is and describe
the basic function it performs.<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2: Demonstrate understanding of the role and importance of
accounting information systems in the various types of business and other
organisations. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3. Identify information system documentation techniques and their
use to understand, evaluate, and document an accounting information systems. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4. Explain the difference between database and file-based
systems. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A5: Discuss the relational database systems and informatively
analyse and interpret accountant’s role of database systems development. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A6: Describe the basic business activities and related data
processing operations performed in the accounting cycles.<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A7: Identify and explain control procedures.<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;&ZeroWidthSpace;</span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: Review and illustrate the purpose, context and functions of
accounting information systems in business practices. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: Critically assess the impact and effective use of information
systems in organisations for competitive advantage. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3: Explain, analyse and apply the mechanism of system
documentation techniques in the accounting cycle. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B4. Compare approaches to AIS including Enterprise Information,
Enterprise Resource Planning, etc. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B5- Formulate a vision of the future and explain the evolving
importance of AIS and Internal Controls due to the guidance and direction of
Public Company Accounting Oversight Board (PCAOB) pronouncements.</span></p><p><br>&nbsp;</p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: Prepare system documentation, and use data flow diagrams and
flowcharts to understand, evaluate, and document information systems. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Design, implement, and effectively use relational database
systems using MS-Access &ZeroWidthSpace;</span><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><br></span></p><p>&nbsp;<br></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Crucial participating in systems analysis and design. </span></p>

<span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;font-size:13px;">D2: Accounting systems
are studied from an accounting cycles perspective, emphasizing the nature and
relevance of accounting internal controls and the relationship of accounting
systems to the functional areas of accounting.</span><br></td>
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
                    ACC302&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Principles of Auditing &amp; Assurance Services <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The course describes the role of the public accountant, professional standards, professional ethics, legal liability, audit evidence and documentation, audit planning internal control, audit sampling &amp; procedures to audit the financial statements. This course thus aims to provide an introduction to the principles and practices of auditing.
It provides students with a sound understanding of fundamental auditing concepts and procedures, and the application of auditing standards. Accordingly, the course provides a foundation for students, who intend pursuing a specialised pathway in the auditing profession, as well as those who will pursue careers in accounting and other disciplines where principles of risk assessment, systems control and evaluation, and transaction testing are important. While the course focuses mainly on the practical application of an external financial audit.
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
								<span class="modal-title">Principles of Auditing &amp; Assurance Services</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>ACC302</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Principles of Auditing &amp; Assurance Services</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B291 and B292</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>The course describes the role of the public accountant, professional standards, professional ethics, legal liability, audit evidence and documentation, audit planning internal control, audit sampling &amp; procedures to audit the financial statements. This course thus aims to provide an introduction to the principles and practices of auditing.
It provides students with a sound understanding of fundamental auditing concepts and procedures, and the application of auditing standards. Accordingly, the course provides a foundation for students, who intend pursuing a specialised pathway in the auditing profession, as well as those who will pursue careers in accounting and other disciplines where principles of risk assessment, systems control and evaluation, and transaction testing are important. While the course focuses mainly on the practical application of an external financial audit.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;This is an AOU based course. The goals of the providers of information may run somewhat counter to those of the users of information. Accordingly there is recognition of the social need for independent public accountants-individuals of professional competence and integrity who can tell us whether the information that we use constitutes a fair picture of what is really going on.<br>On successful completion of BS312 course, students should be able to: 1) Determine an understanding of Certified Public Accountants, Professional standards, and Fundamental audit concepts. 2) Apply a range of audit procedures. 3) Apply auditing standards. 4) Demonstrate an understanding of the legal context within which auditing occurs.&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><div class="ms-rtedir" dir="ltr"><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><b>A. Knowledge
and understanding</b></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1 :<span>&nbsp; </span>Awareness and
understanding of the role of the public accountant , audit standards, ethics ,
liability , audit evidence , documentation , audit planning, internal control ,
audit sampling </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2: Demonstrate the ability to audit financial statements based on
the standards and procedures A3:<span>&nbsp; </span>Audit
of The Sales and Collection Cycle. A4: Audit of The Acquisition and Payment
Cycle </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: Understand the purpose of auditing and be able to investigate
and identify procedures Plan the audit, investigate evidence &amp; identify
procedures. B2: Acquire understanding of the audit standards and how to apply
them in the audit process B3: Be able to distinguish between the different
types of audit reports and which report is mostly applicable for each
situation. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B4: Be able to identify the environmental influences that might
impact the auditor’s plan and opinion.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: Perform basic audit based on auditing standards &amp; GAAP. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Perform audit procedures </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3: Establish a relationship between the audit process and
environmental influences</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Select appropriate procedures for auditing financial statement
accounts </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2: Prepare an audit program of a typical firm </span></p>

<span class="ms-rteFontSize-2" lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D3: Ability to dig out
evidence from a variety of sources in order to achieve the specific audit
objectives of financial statement accounts.</span>&nbsp;</div></td>
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
                    AR111&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Arabic Communication Skills (I) <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    	
AR111 is three credit hour university requirements. It aims to enable students to acquire the Arabic language skills needed at university level, specifically: Arabic syntactic structures, grammatical inflection and case ending in spoken and written Arabic, ability to read Arabic texts in different disciplines, adequate training in writing and using dictionary
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
											<td>	
AR111 is three credit hour university requirements. It aims to enable students to acquire the Arabic language skills needed at university level, specifically: Arabic syntactic structures, grammatical inflection and case ending in spoken and written Arabic, ability to read Arabic texts in different disciplines, adequate training in writing and using dictionary</td>
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
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_88">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_88" class="modal fade" role="dialog">
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
                    B 324&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Marketing and Society <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This course explores the theory and practice of responsible marketing, addressing the interrelated areas of corporate social responsibility and marketing ethics and the emergent area of social marketing. It examines the impact of established marketing techniques and practices on the promotion of social well-being and behavioural change. You will identify key ethical issues involved in marketing decision-making and the responsibilities of organisations to their stakeholders, including the wider community. Elements of marketing management (such as communications, research and planning) are examined within this wider framework at both a domestic and international level.  
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_3">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_3" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Marketing and Society</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B 324</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Marketing and Society</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B205B</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This course explores the theory and practice of responsible marketing, addressing the interrelated areas of corporate social responsibility and marketing ethics and the emergent area of social marketing. It examines the impact of established marketing techniques and practices on the promotion of social well-being and behavioural change. You will identify key ethical issues involved in marketing decision-making and the responsibilities of organisations to their stakeholders, including the wider community. Elements of marketing management (such as communications, research and planning) are examined within this wider framework at both a domestic and international level.  </td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p style="line-height:115%;"><span class="ms-rteThemeFontFace-1" lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:13px;">&ZeroWidthSpace;Marketing
and Sociology. It is a level three course of the B.A. (Hons) in Business
Studies with marketing degree.&nbsp;&ZeroWidthSpace;</span></p>

<p>This course will develop student's ability to synthesise arguments and assumptions from a variety of sources and perspectives, critically evaluate them and apply relevant concepts in a range of contexts. In particular, student will learn concepts, theories and debates about the roles and responsibilities of marketing in society: <br></p><ul><li>Identification and critical analysis of relevant issues involved in responsible marketing</li><li>Application of marketing thinking to health and social behaviour </li><li>Application of responsible marketing to own professional context</li><li>Sensitivity to the problems and challenges in both commercial and social marketing. </li><li>Explore how marketing concepts and techniques can be applied to the marketing of social issues as opposed to the more traditional area of commercial marketing;</li><li>Examine how social marketing approaches can change behaviour in order to achieve socially desirable goals;</li><li>Illustrate, through case study examples, the application of concepts and techniques to 'real world' social marketing problems.&nbsp;<br></li></ul><div>The course is a new development in the optional courses of the BA Business Studies Programme.&nbsp; Marketing in Society will build upon the students understanding of aspects of marketing gleaned from earlier courses within the programme but will focus on the importance of responsible marketing.&nbsp; <br><br>Students will learn to integrate and use information and/or data appropriately in complex contexts. They will also learn to recognise the limitations of knowledge in the area. The course will provide you with opportunities to develop skills in effective communication of ideas and arguments to relevant audiences. You'll be encouraged to manage your learning and reflect on your development as an independent learner.&nbsp;<br><br>The principal learning method used in the course will be problem-based. Usually, students will encounter a short or long case study. They will be expected to make sense of, discuss, analyse, synthesise and evaluate issues and possibilities in the case study. You'll do this by applying your existing knowledge and any new knowledge you can gather from the supplied textbooks, journal articles, electronic sources and course participants. You'll gain knowledge and understanding in the areas of ethics, corporate social responsibility, social marketing, and ethical issues in commercial marketing. The way you are assessed and what you will be assessed on will mirror how you learn and what you learn; the assessment will constitute part of the learning.<br></div></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><strong>&ZeroWidthSpace;</strong><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>A. Knowledge
and understanding</strong></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1: To
understand and apply concepts, theories and debates about the roles and
responsibilities of marketing in society to real life situations </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2: Apply
marketing thinking to the field of health and social behaviour </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3:
Demonstrate an understanding about ethics and marketing </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4: Green and
environmental marketing, sustainability, fair trade and ethical consumption </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: Evaluate the relevance of course concepts to a variety of
other contexts </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2 Synthesise and critical evaluate arguments and assumptions from
a variety of sources and competing perspectives </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3. Recognise the limitations of knowledge in the area </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: Apply responsible marketing to their own professional context
or one they are familiar with C2:Demonstrate a sensitivity to the problems and
challenges in both commercial and social marketing</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Identify and critically analyse relevant<span> </span>issues involved in responsible
social<span> </span>and commercial
marketing </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2: Effectively communicate ideas and arguments to relevant
audiences </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D3: Integrate and use information and/or data in complex contexts </span></p>

<span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;font-size:13px;">D4: Manage own learning
and reflect on their development as an independent learner</span>&ZeroWidthSpace;<br></td>
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
                    B122&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;An Introduction to Retail management and Marketing <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    It is an introductory Level 1 course. As the retail industry is highly dynamic and innovative, this
course looks at how retailing has developed within a business context, and how retail outlets work and apply retail marketing. It offers a balance between theory and practice that is innovative and engaging. During your studies you will consider contemporary factors that affect retailing: globalization; the impact of ever-changing technology; and social and ethical issues. This course is designed for retail industry employees wishing to develop a career in management, and anyone interested in working in the retail sector, or simply wanting to know more about the world of retailing.

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
								<span class="modal-title">An Introduction to Retail management and Marketing</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B122</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>An Introduction to Retail management and Marketing</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>BUS110</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>It is an introductory Level 1 course. As the retail industry is highly dynamic and innovative, this
course looks at how retailing has developed within a business context, and how retail outlets work and apply retail marketing. It offers a balance between theory and practice that is innovative and engaging. During your studies you will consider contemporary factors that affect retailing: globalization; the impact of ever-changing technology; and social and ethical issues. This course is designed for retail industry employees wishing to develop a career in management, and anyone interested in working in the retail sector, or simply wanting to know more about the world of retailing.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;The academic aims of this module is to introduce you to the main functions and management of<br></p><p>a retail business and the key issues associated with understanding retail trading and retail</p><p>environments. After studying the course, you should be able to:</p><ul><li>Explain relevant theories and concepts of retailing</li><li>Describe the key elements of a retail business and the retail trading environment</li><li>Discuss issues associated with operating a business in a retail environment/context</li><li>Outline the key course topics and explain why each topic is important to understanding the principles of retail management</li><li>Explain linkages between components of the course</li><li>Organise your studies, including paper-based and computer-based services</li></ul><p>Continue to develop your awareness of how you learn and how different elements of the course applied to your individual learning style.<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>&ZeroWidthSpace;A. Knowledge
and understanding</strong></span></p><p><span lang="EN-GB">A1: retail technology, which focuses on the
virtual world of e-retailing;</span></p><p><span lang="EN-GB">A2: the diversity of retail products and
sectors;</span></p><p><span lang="EN-GB">A3: retail ethics and the environmental
impact;</span></p><p style="text-align:justify;"><span lang="EN-GB">A4: the
implications of globalisation</span><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: Reflection and critical engagement into both domestic retail technology
and e-retailing</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: Critical thinking, analysis, and synthesis</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3: Valuation
and comparison of retail management.</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><br></span>&nbsp;</p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical
and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: Time management, skills appropriate to business, such as
creativity, persuasion and attractiveness.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Study skills, learning to learn and reflecting on students’
own development as learners.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3: The ability to analyse work-related cases and situations to
identify challenges for organisations in developing responses in relation to
their environments.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C4: The application of course ideas to students’ own interactions
with organisations and life experiences.</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D Key
transferable skills</strong></span></p>

<p>D1: Decision making and problem solving making a viable approach to students to engage with data analysis, interpretation and extrapolation.</p><p>D2: Immerse in related information, arguments and ideas.</p><p>D3: Identify some of the key strengths and needs of their own learning and identify opportunities to address these.&ZeroWidthSpace;&nbsp;</p></td>
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
                    B123&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Management Practice <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This course introduces management ideas and uses activities to build on existing knowledge and skills through the application of management theory. It’s suitable if you’ve studied any introductory course and want to complete the Certificate in Business Studies or gain 30 credits towards our BA (Hons). This introductory Level 1 course introduces management ideas and uses activities to build on your existing knowledge and skills. You’ll also use your own workplace experiences to develop an academic understanding of management and valuable study skills, which you’ll demonstrate by writing about management and reflecting on your own skills as a learner.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_5">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_5" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Management Practice</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B123</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Management Practice</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>BUS110</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This course introduces management ideas and uses activities to build on existing knowledge and skills through the application of management theory. It’s suitable if you’ve studied any introductory course and want to complete the Certificate in Business Studies or gain 30 credits towards our BA (Hons). This introductory Level 1 course introduces management ideas and uses activities to build on your existing knowledge and skills. You’ll also use your own workplace experiences to develop an academic understanding of management and valuable study skills, which you’ll demonstrate by writing about management and reflecting on your own skills as a learner.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><div dir="ltr" style="text-align:left;"><span class="ms-rteFontSize-2" id="ms-rterangepaste-start"></span></div><p dir="ltr" style="text-align:left;"><span class="ms-rteFontSize-2" id="ms-rterangepaste-start"></span><span class="ms-rteFontSize-2" lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">By the
end of this course you’ll have developed a new, more theoretical understanding
of how and why managers do what they do in organisations. You’ll build a
toolkit of management concepts, theories and models that you can use to tackle
workplace issues. You’ll also feel more confident in embarking on further
undergraduate study.</span>&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A. Knowledge
and understanding</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1. Demonstrated how learning they have undertaken previously in
the workplace can be utilised to inform the development of their management
practice </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2. Selected and used a range of management theories, concepts and
ideas to help identify, analyse and address issues and situations in their
current practice setting. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3. Worked in collaboration with others in assessing the
applicability of selected management theories, etc. to their own and others’
identified practice problems.</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4. Reflected
on the impact of their learning on their practice of management, and their
future development as a management practitioner.</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B. Cognitive
skills</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1. Identify and draw upon appropriate forms of prior learning
relating to the development of their management practice. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2. Apply relevant theoretical knowledge of management to a
practical problem. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3. Collaborate with peers’ practitioners to, and begin to,
critically evaluate the applicability of selected management theories etc. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B4. Reflect productively on the development of their practice of
management. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C. Practical and professional skills</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1. Communicate their understanding of management theory and its
application to practice in writing.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2. Work independently on identifying issues and situations in the
workplace and apply academic theories and concepts to these to gain a deeper
understanding of them. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D. Key transferable skills.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1. Use of a range of tools and websites for finding and recording
information online: internet browsers, search engines, copy/ paste, e-portfolios
and download functions </span></p>

<span class="ms-rteFontSize-2" lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2. Communicate with
peer learners via synchronous and asynchronous online media.</span>&ZeroWidthSpace;<br></td>
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
                    B124&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fundamentals of Accounting <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module provides a broad introduction to accounting study at the university level.  It covers the fundamentals of financial and management accounting as well as the essential skills, knowledge and ethics required to be a professional accountant. Fundamentals of Accounting module is required for all business with accounting track. It is strongly recommended that students study this module before Financial accounting (B291) and Management accounting (B292). &ZeroWidthSpace;&ZeroWidthSpace;
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
								<span class="modal-title">Fundamentals of Accounting</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B124</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Fundamentals of Accounting</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>BUS110</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module provides a broad introduction to accounting study at the university level.  It covers the fundamentals of financial and management accounting as well as the essential skills, knowledge and ethics required to be a professional accountant. Fundamentals of Accounting module is required for all business with accounting track. It is strongly recommended that students study this module before Financial accounting (B291) and Management accounting (B292). &ZeroWidthSpace;&ZeroWidthSpace;</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:13px;">&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;It aims to equip students with the essential principles of measuring management performance and improving financial planning, control and decision-making. Students can gain an understanding of financial reports through their preparation, based on the double-entry bookkeeping system which is essential for the management of any organisation.&nbsp; &ZeroWidthSpace;</span>&ZeroWidthSpace;<br></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong>A. Knowledge and understanding</strong></p><p style="text-align:justify;"><strong>A1</strong>: Awareness and understanding of the role of accounting in business and other organisations and of its theory, principles, concepts, practices, techniques, ethics, limitations, and techniques central to bookkeeping and accounting.<br></p><p style="text-align:justify;"><strong>A2: </strong>Demonstrate the ability to prepare financial statements based on application of accounting concepts, regulations and principles.</p><p style="text-align:justify;"><strong>A3</strong>: Demonstrate understanding of the types of costs and how they behave in order to calculate cost-volume-profit relationships, </p><p style="text-align:justify;"><strong>A4</strong>: Demonstrate understanding of management's decision-making process as it relates to product pricing, production, adding and dropping, etc.</p><p style="text-align:justify;"><strong>A5</strong>: Demonstrate understanding of the types of budgets and be able to prepare operating budgets, financial budgets and capital budgets.</p><p style="text-align:justify;"><strong>A6:</strong> Demonstrate understanding of the responsibility centers and balanced scorecard.<br></p><p><br><strong>B. Cognitive skills</strong></p><p style="text-align:justify;"><strong>B1</strong>: Review and illustrate the purpose, context and environmental influences and constraints on financial accounting and business practices.</p><p style="text-align:justify;"><strong>B2</strong>: Explain the balance sheet equation, the basic financial statements and the information conveyed in each of the statements. </p><p style="text-align:justify;"><strong>B3</strong>: Explain the steps in the accounting cycle for service and merchandising companies.</p><p style="text-align:justify;"><strong>B4:</strong> Explain the relevant factors in making different decisions.</p><p style="text-align:justify;"><strong>B5</strong>: Explain methods that don't use present value versus those that do use present value </p><p style="text-align:justify;"><strong>B6</strong>: Explain the features of responsibility reports and differentiate between cost centres, profit centres and investment centres.<br></p><p><strong>C. Practical and professional skills</strong>&ZeroWidthSpace;</p><p style="line-height:115%;text-indent:-19.7pt;margin-left:19.7pt;"><span class="ms-rteThemeFontFace-1 ms-rteThemeForeColor-2-5" style="font-size:13px;"><span lang="EN-GB" style="line-height:115%;"><strong>C1:</strong></span><span lang="EN-GB" style="line-height:115%;"> Record transactions
and events, and maintain accounting records as required for bookkeeping and
accounting.</span></span></p>

<p style="line-height:115%;text-indent:-19.7pt;margin-left:19.7pt;"><span style="font-size:13px;"><strong><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;">C2: </span></strong><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;">Prepare basic
financial statements based upon Generally Accepted Accounting Principles.</span></span></p><p style="line-height:115%;text-indent:-19.7pt;margin-left:19.7pt;"><span style="font-size:13px;"><strong><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;">C3</span></strong><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;">: Develop the
general practical and professional skills of management accounting that can be
used for personal and career goals.</span></span></p>

<p><strong>D Key transferable skills&nbsp;</strong></p><p><strong>D1</strong>: Use simple mathematics for the purpose of calculations in bookkeeping, accounting and preparing/analysing financial statements, including basic ratio analysis.<br></p><p><strong>D2</strong>: Compare critically and use different approaches to issues and problems within management accounting.<br></p><p><strong>D3</strong>: Communicate management accounting information effectively and appropriately.&ZeroWidthSpace;<br></p><p><strong>D4</strong>: Use fundamental business mathematics and other quantitative methods effectively and appropriately.<br></p></td>
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
                    B205A&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Exploring innovation and entrepreneurship <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module provides students with a broad foundation in innovation and entrepreneurship. The course is composed of two parts A and B. Part A of it comprises 14 study weeks (one semester). And is structured into 2 (out of the five) linked blocks. It also forms part of the new undergraduate qualification BA Business Management and BA Business Marketing. Students will be introduced to core concepts of entrepreneurship and innovation. They will also examine the theoretical and practical connections between these distinct yet closely-interrelated fields of study.

Block 1: Core concepts
Introduces core concepts of innovation and entrepreneurship and gives the student an opportunity to examine ‘what it all means for me’. It also introduces students to each other, creates confidence, and promotes teambuilding in preparation for Block 2.

Block 2: Teams and networks
Block 2 focuses on the skills required to create teams, build networks and to secure the necessary resources in the context of an innovative, entrepreneurial venture. It also introduces and develops the underpinning knowledge and understanding on key areas, including teams, networks, resource acquisition and legitimacy-building, in preparation for the new venture creation activity (Block 4 of B205B).
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
								<span class="modal-title">Exploring innovation and entrepreneurship</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B205A</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Exploring innovation and entrepreneurship</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B207B</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module provides students with a broad foundation in innovation and entrepreneurship. The course is composed of two parts A and B. Part A of it comprises 14 study weeks (one semester). And is structured into 2 (out of the five) linked blocks. It also forms part of the new undergraduate qualification BA Business Management and BA Business Marketing. Students will be introduced to core concepts of entrepreneurship and innovation. They will also examine the theoretical and practical connections between these distinct yet closely-interrelated fields of study.

Block 1: Core concepts
Introduces core concepts of innovation and entrepreneurship and gives the student an opportunity to examine ‘what it all means for me’. It also introduces students to each other, creates confidence, and promotes teambuilding in preparation for Block 2.

Block 2: Teams and networks
Block 2 focuses on the skills required to create teams, build networks and to secure the necessary resources in the context of an innovative, entrepreneurial venture. It also introduces and develops the underpinning knowledge and understanding on key areas, including teams, networks, resource acquisition and legitimacy-building, in preparation for the new venture creation activity (Block 4 of B205B).</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;B205A academic aim is to introduce students to number of fundamental concepts and theories of entrepreneurial innovation. It also re-apply some generic business and management concepts in an entrepreneurial and innovation-related concept (e.g. entrepreneurial marketing and entrepreneurial finance. The coverage of innovation and entrepreneurship subjects will be wide-ranging and integrative, with the aim of providing the necessary foundations for interested students to progress to a more in-depth study of specialist topics within this subject area during their level 3 studies. <br></p><p>Progression is also addressed within B205A - with a gradual development of knowledge and skills from Block 1 and Block 2 (covered in Part A of the course) through Block 3, Block 4 and Block 5 (covered in Part B of the course, B207B). There will be a logical progression of subject matter, from an introduction to core concepts in innovation and entrepreneurship (Block 1), followed by a more skills-oriented examination of teams, networks and associated concepts (Block 2), a comparative study of innovation and entrepreneurship in different contexts (Block 3), a simulated experience of entrepreneurial team-working and innovation (Block 4) and an opportunity for reflection and integration (Block 5). Study and employment skills will be integrated into the learning activities, with a particular focus on digital literacy, creative thinking and problem solving, team-working, persuasive communication and more general personal development and enterprise-related skills. <br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><b>A. Knowledge
and understanding</b></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1: knowledge
of different forms of innovative and entrepreneurial practice around the world
and at different scales, including: technological and social innovation;
commercial and social enterprise; independent and corporate entrepreneurship. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2: understand
different research perspectives on innovation and entrepreneurship, recognising
that these subjects can be studied at multiple levels of analysis. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3:
familiarize with core theories, concepts and frameworks that have been applied
to innovation and entrepreneurship, with a particular focus on their
implications for practice. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4: Know the
relationship between innovation and entrepreneurship, both at a conceptual and
a practical level. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: Distinguish the key components of innovative and
entrepreneurial processes and practices kinds (i.e. in comparison with more
routinised approaches) </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: Select innovative and entrepreneurial approaches that are
likely to be appropriate in particular organisational contexts. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills&ZeroWidthSpace;</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span>C1: Identify, search for
and pursue entrepreneurial opportunities, with the aim of creating sustainable
business models. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Negotiate, influence, and gain legitimacy in an
entrepreneurial setting. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3: Engage in creative problem-solving. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C4: Apply design thinking approaches in order to develop practical
solutions. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C5: Deploy effective networking and persuasive communication
skills. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Work constructively and ethically in entrepreneurial settings,
which may be characterised by ambiguity, complexity and open-ended challenges. </span></p>

<span class="ms-rteFontSize-2" lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2: Display resilience
and an on-going capacity to learn from direct personal experiences, and those
of others.</span><br></td>
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
                    B205B&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Exploring innovation and entrepreneurship <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module provides students with a broad foundation in innovation and entrepreneurship. The course is composed of two parts A and B. Part A of it comprises 14 study weeks (one semester). And is structured into 2 (out of the five) linked blocks. It also forms part of the new undergraduate qualification BA Business Management and BA Business Marketing. Students will be introduced to core concepts of entrepreneurship and innovation. They will also examine the theoretical and practical connections between these distinct yet closely-interrelated fields of study.
Block 1: Core concepts
Introduces core concepts of innovation and entrepreneurship and gives the student an opportunity to examine ‘what it all means for me’. It also introduces students to each other, creates confidence, and promotes teambuilding in preparation for Block 2.
Block 2: Teams and networks
Block 2 focuses on the skills required to create teams, build networks and to secure the necessary resources in the context of an innovative, entrepreneurial venture. It also introduces and develops the underpinning knowledge and understanding on key areas, including teams, networks, resource acquisition and legitimacy-building, in preparation for the new venture creation activity (Block 4 of B205B).

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_8">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_8" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Exploring innovation and entrepreneurship</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B205B</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Exploring innovation and entrepreneurship</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B207B</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module provides students with a broad foundation in innovation and entrepreneurship. The course is composed of two parts A and B. Part A of it comprises 14 study weeks (one semester). And is structured into 2 (out of the five) linked blocks. It also forms part of the new undergraduate qualification BA Business Management and BA Business Marketing. Students will be introduced to core concepts of entrepreneurship and innovation. They will also examine the theoretical and practical connections between these distinct yet closely-interrelated fields of study.
Block 1: Core concepts
Introduces core concepts of innovation and entrepreneurship and gives the student an opportunity to examine ‘what it all means for me’. It also introduces students to each other, creates confidence, and promotes teambuilding in preparation for Block 2.
Block 2: Teams and networks
Block 2 focuses on the skills required to create teams, build networks and to secure the necessary resources in the context of an innovative, entrepreneurial venture. It also introduces and develops the underpinning knowledge and understanding on key areas, including teams, networks, resource acquisition and legitimacy-building, in preparation for the new venture creation activity (Block 4 of B205B).
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;B205A academic aim is to introduce students to number of fundamental concepts and theories of entrepreneurial innovation. It also re-apply some generic business and management concepts in an entrepreneurial and innovation-related concept (e.g. entrepreneurial marketing and entrepreneurial finance. The coverage of innovation and entrepreneurship subjects will be wide-ranging and integrative, with the aim of providing the necessary foundations for interested students to progress to a more in-depth study of specialist topics within this subject area during their level 3 studies. <br></p><p>Progression is also addressed within B205A - with a gradual development of knowledge and skills from Block 1 and Block 2 (covered in Part A of the course) through Block 3, Block 4 and Block 5 (covered in Part B of the course, B207B). There will be a logical progression of subject matter, from an introduction to core concepts in innovation and entrepreneurship (Block 1), followed by a more skills-oriented examination of teams, networks and associated concepts (Block 2), a comparative study of innovation and entrepreneurship in different contexts (Block 3), a simulated experience of entrepreneurial team-working and innovation (Block 4) and an opportunity for reflection and integration (Block 5). Study and employment skills will be integrated into the learning activities, with a particular focus on digital literacy, creative thinking and problem solving, team-working, persuasive communication and more general personal development and enterprise-related skills. <br><br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>A. Knowledge
and understanding</strong></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1: knowledge
of different forms of innovative and entrepreneurial practice around the world
and at different scales, including: technological and social innovation;
commercial and social enterprise; independent and corporate entrepreneurship. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2: understand
different research perspectives on innovation and entrepreneurship, recognising
that these subjects can be studied at multiple levels of analysis. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3:
familiarize with core theories, concepts and frameworks that have been applied
to innovation and entrepreneurship, with a particular focus on their
implications for practice. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4: Know the
relationship between innovation and entrepreneurship, both at a conceptual and
a practical level. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: Distinguish the key components of innovative and
entrepreneurial processes and practices kinds (i.e. in comparison with more
routinised approaches) </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: Select innovative and entrepreneurial approaches that are
likely to be appropriate in particular organisational contexts. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills&ZeroWidthSpace;</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span>C1: Identify, search for
and pursue entrepreneurial opportunities, with the aim of creating sustainable
business models. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Negotiate, influence, and gain legitimacy in an
entrepreneurial setting. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3: Engage in creative problem-solving. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C4: Apply design thinking approaches in order to develop practical
solutions. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C5: Deploy effective networking and persuasive communication
skills.&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><br></span>&nbsp;</p>

<p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Work constructively and ethically in entrepreneurial settings,
which may be characterised by ambiguity, complexity and open-ended challenges. </span></p>

<span class="ms-rteFontSize-2" lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2: Display resilience
and an on-going capacity to learn from direct personal experiences, and those
of others.</span><span class="ms-rteFontSize-2">&ZeroWidthSpace;</span><span class="ms-rteFontSize-2" id="ms-rterangepaste-end"></span>&ZeroWidthSpace;<br></td>
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
                    B207A &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Shaping Business Opportunities I <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    B207A is an 8-credit (30 points), Level 5 UK-OU based course offered through the Business Program at the Arab Open University as a compulsory course for all students enrolled in all tracks in the program. Entry into this course is contingent upon the successful completion of BS110. The B207 module in this new study plan is equivalent to B203 module in the old study plan (which is itself previously equivalent to B202)
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
								<span class="modal-title">Shaping Business Opportunities I</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B207A </td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Shaping Business Opportunities I</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>BS110</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>B207A is an 8-credit (30 points), Level 5 UK-OU based course offered through the Business Program at the Arab Open University as a compulsory course for all students enrolled in all tracks in the program. Entry into this course is contingent upon the successful completion of BS110. The B207 module in this new study plan is equivalent to B203 module in the old study plan (which is itself previously equivalent to B202)</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;This module is designed to provide intermediate conceptual and practical learning to students in operations management, marketing and human resource management. The module comprises 16 study weeks (including final assessment). <br></p><p>&ZeroWidthSpace;<br></p><p><span lang="EN-GB" style="text-decoration:underline;">&ZeroWidthSpace;Operations Management: (4 weeks)</span></p><p>The following subjects will be covered: </p><ul><li>Introduction to operations management</li><li>Operations strategy</li><li>Product, service and process design</li><li>International location of operations</li><li>Global supply chain</li><li>Operations: changing market conditions</li></ul><div>Operations: risk and resilience<br><br>&nbsp;<br><br><span lang="EN-GB" style="text-decoration:underline;">&ZeroWidthSpace;&ZeroWidthSpace;Marketing: (6</span><span lang="EN-GB" style="text-decoration:underline;"> weeks)</span><br><br>The following subjects will be covered:</div><ul><li>Marketing: purpose and mission</li><li>Marketing (external environment, brand formulation, segmentation and targeting, market research)</li><li>Analysing market growth potential</li><li>International marketing and global branding</li><li>Consumer behaviour</li><li>Business-to-business marketing</li></ul><div>Marketing (integrated marketing; lifecycle maturity, product portfolio, brand refreshing, monitoring and measuring success, crisis management)<br><br><br><br><span lang="EN-GB" style="text-decoration:underline;">Human Resource Management (3 weeks)</span><br></div><ul><li>What does it mean to move from employee relations to HRM in a global context?</li><li>Employment relations</li><li>Change management&ZeroWidthSpace;<br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong>A. Knowledge and understanding</strong></p><p><strong>A1</strong>:&nbsp; Develop a critical appreciation of the interactions between various business functions (operations management, marketing and human resource management) and the integrative complexity that shapes business innovation.</p><p><strong>A2</strong>: Develop a critical understanding of why new products and services are imperative to contemporary business practice. Also to develop knowledge and understanding of external issues affecting the successful running of organizations, including how they compete in a global context.<br></p><p><strong>A3: </strong>Develop knowledge and understanding of the elements required to build long-term success in organizations, and how students can contribute to the fostering of long-term value creation.</p><p><strong>A4: </strong>develop knowledge and critical understanding of the theories, concepts and models of different business functions (operations management, marketing and human resource management).</p><p></p><p><strong>B. Cognitive skills</strong><br></p><p><strong>B1: </strong>Select and<strong> </strong>critically analyse information relevant to a particular problem or issue related to business and management.</p><p><strong>B2/B3: </strong>Evaluate and compare competing perspectives, theoretical models and concepts in the context of practical situations</p><p><strong>B2/B4: </strong>Gather and synthesise material from a variety of sources in constructing arguments applied to business and management <br></p><p><strong>C. Practical and professional skills</strong><br></p><p></p><p><strong>C3</strong>: Communicate in a professional manner in written work, face to face and online. Plan, monitor and review progress as independent learner, including a focus on personal skills development.</p><p><strong>C4: </strong>Develop an awareness of ethical issues and professional standards relevant to business and management<br></p><p><strong>D Key transferable skills&nbsp;</strong></p><p><strong>D2: </strong>Search for and use relevant digital and non-digital information from sources other than the module materials.</p><p><strong>D3: </strong>Compare critically and use different approaches to issues and problems within business management. Engage in critical reflection.</p><p><strong>D4: </strong>Consolidate an understanding of academic language and literacy practices in order to effectively engage with the academic knowledge and skills of Level 5 study.<br></p></td>
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
                    B207B&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Shaping Business Opportunities  <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    B207B is an 8-credit (30 points), Level 5 UK-OU based course offered through the Business Program at the Arab Open University as a compulsory course for all students enrolled in all tracks in the program. Entry into this course is contingent upon the successful completion of B207A. 
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_51">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_51" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Shaping Business Opportunities </span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B207B</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Shaping Business Opportunities </td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B207A</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>B207B is an 8-credit (30 points), Level 5 UK-OU based course offered through the Business Program at the Arab Open University as a compulsory course for all students enrolled in all tracks in the program. Entry into this course is contingent upon the successful completion of B207A. </td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p><span style="font-size:13px;"><span lang="EN-GB" style="font-family:&quot;arial&quot;,sans-serif;">&ZeroWidthSpace;This
module is designed to provide intermediate conceptual and practical learning to
students in management and accounting. The module comprises 16 study weeks
(including final assessment). </span>&ZeroWidthSpace;<br></span></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong>A. Knowledge and understanding</strong></p><p style="text-align:justify;"><strong>A1</strong>:&nbsp; Develop a critical appreciation of the interactions between various business functions (management and accounting) and the integrative complexity that shapes business innovation.<br></p><p style="text-align:justify;"><strong>A2: </strong>Develop knowledge and understanding of the elements required to build long-term success in organizations, and how students can contribute to the fostering of long-term value creation.<br></p><p style="text-align:justify;"><strong>A3: </strong>develop knowledge and critical understanding of the theories, concepts and models of different business functions.</p><p style="text-align:justify;"><strong>B. Cognitive skills</strong><br></p><p></p><p style="text-align:justify;"><strong>B1: </strong>Select and<strong> </strong>critically analyse information relevant to a particular problem or issue related to business and management.<br></p><p style="text-align:justify;"><strong>B2: </strong>Evaluate and compare competing perspectives, theoretical models and concepts in the context of practical situations<br></p><p><strong>B3: </strong>Gather and synthesise material from a variety of sources in constructing arguments applied to business and management <br></p><p><strong>C. Practical and professional skills</strong></p><p><strong>C1</strong>: Communicate in a professional manner in written work, face to face and online. Plan, monitor and review progress as independent learner, including a focus on personal skills development.<br></p><p><strong>C2: </strong>Develop an awareness of ethical issues and professional standards relevant to business and management<br></p><p><strong>D Key transferable skills </strong></p><p><strong>D1: </strong>Search for and use relevant digital and non-digital information from sources other than the module materials.</p><p style="text-align:justify;"><strong>D2: </strong>Compare critically and use different approaches to issues and problems within business management. Engage in critical reflection.&ZeroWidthSpace;<br></p><p><strong>D3: </strong>Consolidate an understanding of academic language and literacy practices in order to effectively engage with the academic knowledge and skills of Level 5 study.<br></p></td>
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
                    B291&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Financial Accounting <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This course is the first of two modules leading to the Professional Certificate in Accounting (K01). We strongly recommend that you study this course before Management accounting (B292), but both courses can be studied independently. This is a Level 2 course and students need to have a good knowledge of financial accounting, obtained either through Level 1 study with the AOU or by doing equivalent work at another university. Ideal preparation for this course would be our Level 1 course Fundamentals of Accounting (B124).
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
								<span class="modal-title">Financial Accounting</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B291</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Financial Accounting</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B124</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This course is the first of two modules leading to the Professional Certificate in Accounting (K01). We strongly recommend that you study this course before Management accounting (B292), but both courses can be studied independently. This is a Level 2 course and students need to have a good knowledge of financial accounting, obtained either through Level 1 study with the AOU or by doing equivalent work at another university. Ideal preparation for this course would be our Level 1 course Fundamentals of Accounting (B124).</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;font-size:12pt;">&ZeroWidthSpace;This
is the course for students if they want a route into the accountancy profession
or need to gain fundamental accounting skills for a management or other role.
Students will gain an understanding of how financial statements are prepared
and develop the skills to prepare financial statements. Students will explore
differences in financial accounting for different businesses, building an
understanding of the frameworks underpinning accounting and audit practice</span>.&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><b>&ZeroWidthSpace;A. Knowledge
and understanding</b></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1:
Demonstrate understanding of the role and importance of accounting in the
various types of business and other organisations. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2:
Demonstrate understanding of the accounting regulatory framework in the UK and
EU as well as within the context of international financial and capital
markets. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3:
Demonstrate understanding of the qualitative characteristics of financial
accounting information, accounting concepts and principles. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4:
Demonstrate the ability to prepare financial statements based on application of
accounting concepts, regulations and principles. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: Review and illustrate the purpose, context and environmental
influences and constraints on financial accounting and business practices (Unit
1). B2: Explain, analyse and apply the mechanism of double-entry bookkeeping
and the accounting cycle (Unit 2). B3: Identify, classify, measure and
summarise the elements of financial statements applying accounting principles
and concepts (Units 3 and 4). B4: Explain and interpret the purpose, form and
content of the three main financial statements; income statement, balance sheet
and cash flow statement (Unit 5). B5: Explain and evaluate the need for ethics
in the behaviour of accountants and the need for independent auditing in the
reporting process of public and large enterprises (Unit 6). B6: Explain and
review the relations between corporate governance,</span><span lang="EN-GB"> </span><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">auditing and
financing (Unit 7). </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: Record transactions and events, and maintain accounting
records manually and gain some familiarity with computerised accounting
software (Units 3 and 4). </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Prepare periodic financial statements for sole traders,
partnerships, non-profit organisations and single-entity private and public
limited companies (Unit 5)</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p>

<span class="ms-rteFontSize-2" lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Use simple
mathematics for the purpose of calculations in bookkeeping, accounting and
preparing/analysing financial statements, including basic ratio analysis.</span><p><br>&nbsp;</p></td>
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
                    B292&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Management Accounting <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This is a level 2 course and students need to have a good knowledge of financial accounting obtained either through level 1 study with the AOU or completing equivalent work at another university. This is the course for students if they want a route into the accounting profession or need to gain fundamental accounting skills  for a management or other role. The overall aim of this module is to help students learn and interpret management accounting information. You may be undertaking this module to prepare for a career as an accountant working in or with organizations, as part of a degree or as a stand- alone module.  
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
								<span class="modal-title">Management Accounting</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B292</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Management Accounting</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B124</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This is a level 2 course and students need to have a good knowledge of financial accounting obtained either through level 1 study with the AOU or completing equivalent work at another university. This is the course for students if they want a route into the accounting profession or need to gain fundamental accounting skills  for a management or other role. The overall aim of this module is to help students learn and interpret management accounting information. You may be undertaking this module to prepare for a career as an accountant working in or with organizations, as part of a degree or as a stand- alone module.  </td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;font-size:12pt;display:none;"></span></p><p style="margin:0in 0in 0pt;text-align:justify;line-height:115%;"><span style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">B292 academic aim is to introduce students to number of fundamental
concepts and theories of Management Accounting in order to guide managerial
decision making by individuals and business units. It also develops the
students’ knowledge of Management Accounting as well as skills in
problem-solving, decision making relating to aspects of planning, costing, budgeting,
evaluating. B292 also prepares students for advanced Management Accounting
concepts. After studying the course, the students should be able to: </span></p><p style="margin:0in 0in 0pt;text-align:justify;line-height:115%;"><span style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">&nbsp;</span></p><ul style="margin-top:0in;"><li style="color:#000000;line-height:115%;font-size:12pt;font-style:normal;font-weight:400;"><span style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">Demonstrate
     understanding of the nature of management and the role of management
     accounting in the management process.</span></li><li style="color:#000000;line-height:115%;font-size:12pt;font-style:normal;font-weight:400;"><span style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">Demonstrate
     understanding of the different types of costs and the role of costs in
     decision making.</span></li><li style="color:#000000;line-height:115%;font-size:12pt;font-style:normal;font-weight:400;"><span style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">Demonstrate understanding
     of how inventory is accounted for and managed within the organization, and
     the methods for calculating the cost of different types of products,
     processes and services.</span></li><li style="color:#000000;line-height:115%;font-size:12pt;font-style:normal;font-weight:400;"><span style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">Demonstrate the
     ability to prepare budgets.</span></li><li style="color:#000000;line-height:115%;font-size:12pt;font-style:normal;font-weight:400;"><span style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">Demonstrate
     understanding of the management and the influence of economic factors and
     economic analysis on management decision making.</span></li></ul>

<p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;font-size:12pt;"></span><br>&nbsp;</p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>A. Knowledge
and understanding</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"></span></p><p><strong>A1</strong> : Demonstrate Understanding of the nature of management and the role of management accounting in the management process.<br></p><p><strong>A2</strong>: Demonstrate the understanding of the different types of costs and the role of costs in decision making.<br></p><p><strong>A3:</strong> Demonstrate understanding of how inventory is accounted for and managed within the organization and the methods for calculating the costs of different types of products , processes and services..<br></p><p style="line-height:115%;"><strong><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">A4:</span></strong><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;"> Demonstrate the ability to prepare
budgets.</span></p>

<p><br>&nbsp;</p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"></span></p><p style="text-align:justify;"><strong>B1.</strong> Understand the nature of organizations, the process of management and the role of information (including accounting information) in managing organizations. (Unit 1).<br></p><p style="text-align:justify;"><strong>B2. </strong>Understand the nature of cost analysis for planning and decision making and be able to apply and explain the techniques covered. (Unit 2).<br></p><p style="text-align:justify;"><strong>B3</strong>. Understand and explain the costing and accounting methods and&nbsp;&nbsp;&nbsp; systems which provide the management of an organization with relevant and reliable information on which to base decisions. (Unit 3).<br></p><p style="text-align:justify;"><strong>B4</strong>. Explain the budgetary process and illustrate in detail a method of preparing budgets for planning and control purposes. (Unit 4).<br><br></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"></span></p><p style="text-align:left;"><strong>C1: </strong>Understand the use of marginal costs , cost volume –profit Analysis and contribution analysis in costing and price decisions.<br><strong>C2:</strong>Calculate costs using the job , process and contract costing <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Methods , calculate the cost of a product or service from basic<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Information using batch and process costing.</p><p style="text-align:left;"><strong>C3:</strong>Prepare budgets and calculate the main variances used in <br>&nbsp;&nbsp;&nbsp;&nbsp; Variance analysis. </p><p style="text-align:left;"><strong>C4</strong>:Be able to prepare accounting statements for planning and <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Control.</p><p style="text-align:left;"><strong>C5:</strong> Be able to prepare periodic reports<br></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"></span></p><p style="text-align:justify;"><strong>D1:</strong>Demonstrate understanding of the nature &amp; types of costs</p><p style="text-align:justify;"><strong>D2:</strong> Calculate Break-even points in units and in turnover.</p><p><strong>D3:</strong> The use of Activity based costing as a more exact method </p><p>In indirect cost allocation.<br></p><p><strong>D4:</strong>Demonstrate ability to prepare different types of budgets&ZeroWidthSpace;<br></p><p><strong>D5</strong>: Work with qualitative &amp; quantitative data drawing appropriate conclusions based on findings.<span class="ms-rteFontSize-2">&ZeroWidthSpace;</span><span class="ms-rteFontSize-2" id="ms-rterangepaste-end"></span>&ZeroWidthSpace;<br></p></td>
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
                    B325&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Managing across organisational and cultural boundaries <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    B325 is offered as an option at level 3 in the awards: BA (Hons) Business Studies; BA (Hons) Leadership and management. The course aligns well within the educational aims of these programs by developing “the student’s interest in and knowledge of the world of business”. By providing students with the opportunity to draw on their own experience and critically engage with theory with theory relevant to managing across organisational and cultural boundaries, it supports the program’s aim of developing “graduates who bring to their employment in business or organisations of any sort, a range of critically important and highly valued skills”. B325 will complement other courses within the existing suite of courses offered within management and business studies. It will embrace all learners irrespective of their level of attained experience and position within their own organisation.
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
								<span class="modal-title">Managing across organisational and cultural boundaries</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B325</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Managing across organisational and cultural boundaries</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>BUS310</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>B325 is offered as an option at level 3 in the awards: BA (Hons) Business Studies; BA (Hons) Leadership and management. The course aligns well within the educational aims of these programs by developing “the student’s interest in and knowledge of the world of business”. By providing students with the opportunity to draw on their own experience and critically engage with theory with theory relevant to managing across organisational and cultural boundaries, it supports the program’s aim of developing “graduates who bring to their employment in business or organisations of any sort, a range of critically important and highly valued skills”. B325 will complement other courses within the existing suite of courses offered within management and business studies. It will embrace all learners irrespective of their level of attained experience and position within their own organisation.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p><span class="ms-rteFontSize-2" id="ms-rterangepaste-start"></span><span class="ms-rteFontSize-2" lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">The
aim of the course is fairly to provide students with ways if understanding and
analysing different organisational, inter- organisational and international
context and the ways in which such different contexts influence individuals’
experience of work. Secondly, the course aims to provide students with
knowledge and understanding of themes and challenges pertaining to organising
and managing across this different context; managing aims, power, politics,
trust, cultural diversity and the darker side of organising. The course
embassies the relationships between theory and practice; putting emphasis on
the theoretical underpinnings and debates surrounding the themes whilst at the
same time requiring students to draw on their own experience. Achieving the
intended learning outcomes (covering both knowledge and skills) fully supports
this dual aim.</span>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>&ZeroWidthSpace;A. Knowledge
and understanding</strong></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1:
Inter-organisational collaboration, organisational behaviour, and international
management theories and concepts relevant to managing across organisational and
cultural boundaries.<span>&nbsp; </span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2: Themes
and challenges pertaining to organizing and managing across intra,
inter-organisational and international contexts including the management of
aims, power, politics, trust, cultural diversity and the darker side of
organising.</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: Use conceptual frameworks to describe functions of organising and
managing in and across organisational and international contexts. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: Identify and critically assess different perspectives on
managing and organising.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3: Synthesise, critically evaluate and challenge course relevant
theories of inter-organisational collaboration, organisational behaviour, and
international management. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B4: Critically evaluate theories in relation to personal
experiences, organisational, inter-organisational and international setting
with which you are familiar and the relative standpoints of others within
different contexts. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: Use and adopt relevant concepts and theories to practically
engage with a range of problems and issues in the work place. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Use specific inter-organisational collaboration,
organisational behaviour, and international management knowledge, cognitive and
key skills developed during the course to enhance individual work / practice.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.&ZeroWidthSpace;</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span>D1: Read and interpret
information presented in a variety of forms including academic journals, books
and on-line text. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2: Articulate ideas and communicate effectively using appropriate
interorganisational collaboration, organisational behaviour, and international
management theories and concepts. D3: Identify and ask questions appropriate to
the exploration and complex concepts.&nbsp;</span></p><p><span class="ms-rteFontSize-2" lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D4: Engage in
reflective, experiential and collaborative learning in face to face and virtual
context.</span>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
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
                    B326&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Advanced Financial Accounting <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Advanced Accounting is a continuation of the study of financial accounting. This course is the last of three modules leading to the Professional Certificate in Accounting. This is a Level 3 course and students need to have a good knowledge of financial accounting, obtained either through Levels 1 and 2 studies. Ideal preparation for this course would be our Level 1 course Financial accounting (BE210) and level 2 course Intermediate financial accounting (B291).
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_13">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_13" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Advanced Financial Accounting</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B326</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Advanced Financial Accounting</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B291</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Advanced Accounting is a continuation of the study of financial accounting. This course is the last of three modules leading to the Professional Certificate in Accounting. This is a Level 3 course and students need to have a good knowledge of financial accounting, obtained either through Levels 1 and 2 studies. Ideal preparation for this course would be our Level 1 course Financial accounting (BE210) and level 2 course Intermediate financial accounting (B291).</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p><span class="ms-rteFontSize-2" lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;The
areas of coverage in this course include issues concerning the operation of
business combinations and consolidated financial statements, and international
accounting issues. Students are expected to develop both an understanding of
the concepts underlying these topics and the technical and analytical skills
needed to apply the concepts in practice. The case method will be used to
supplement problems.</span>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><b>A. Knowledge
and understanding</b></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1: Demonstrate an understanding of current GAAP related to
business combinations and its relationship to present reporting practices.<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2: Demonstrate an understanding of contemporary accounting theory
and practice pertaining to business combinations and corporate consolidations. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3: Demonstrate an understanding of the various methods of
accounting for an investment in equity shares of another company.<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4: Understand concepts related to foreign currency, exchange
rates, and foreign exchange risk.<span>&nbsp; </span>A5: Understand
how foreign currency forward contracts and foreign currency options can be used
to hedge foreign exchange risk.<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A6: Describe guidelines as to when foreign currency financial
statements are to be translated using the current rate method and when they are
to be translated using the temporal method.<span>&nbsp;
</span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: Explain how acquisition expenses are reported.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: Explain the complexities of revenue recognition. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3: the valuation of assets, including goodwill, and liabilities
acquired in a business combination accounted for by the acquisition method. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B4: Analyse and interpret the relevant International Financial
Reporting Standard (IFRS). </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B5: Prepare and analyse accounts for importing and exporting
transactions denominated in foreign currencies, as well as accounting for
forward exchange contracts.<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: Properly prepare consolidated financial statements as of the
date of acquisition and for periods subsequent to the date of acquisition. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Prepare a worksheet to consolidate the accounts of two
companies that form a business combination. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3: Adjust for foreign currency transactions and financial
statements.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.&ZeroWidthSpace;</strong></span></p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;font-size:12pt;"><span class="ms-rteFontSize-2">D1: Use simple mathematics for the purpose of
calculations in bookkeeping, accounting and preparing/analysing financial
statements</span></span>&ZeroWidthSpace;<br></td>
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
                    B327&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creating futures: Sustainable enterprise and innovation <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module is designed to provide intermediate/advanced conceptual and practical learning to students interested in the theory and practice of entrepreneurship and innovation in different contexts. B327 is a new level three course in the B.A. (Hons) in Business Studies with Marketing track. This module is a direct replacement for B322 (Investigating entrepreneurial opportunities). Structured around 4 study blocks, B327 addresses the societal impacts of entrepreneurship and innovation, researching entrepreneurship and innovation, and sustainable enterprise challenge.  
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
								<span class="modal-title">Creating futures: Sustainable enterprise and innovation</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B327</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Creating futures: Sustainable enterprise and innovation</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>BUS310</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module is designed to provide intermediate/advanced conceptual and practical learning to students interested in the theory and practice of entrepreneurship and innovation in different contexts. B327 is a new level three course in the B.A. (Hons) in Business Studies with Marketing track. This module is a direct replacement for B322 (Investigating entrepreneurial opportunities). Structured around 4 study blocks, B327 addresses the societal impacts of entrepreneurship and innovation, researching entrepreneurship and innovation, and sustainable enterprise challenge.  </td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p><span class="ms-rteFontSize-2" lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;The
academic purpose of this module is to enable learners to develop independent
research and online collaborative skills necessary to engage in enterprise and
innovation practices in new and existing organisations. The module encourages
students to do so by articulating how entrepreneurship and innovation can be
used to satisfy individual goals/objectives while contributing to solving
societal problems in an ethical and sustainable manner. The module also
explores the theoretical and practical connections between the distinct yet
closely-interrelated fields of study.</span>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>A. Knowledge
and understanding</strong></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1: Create
and manage sustainable forms of innovative and entrepreneurial ventures within
a range of specialist areas, such as Engineering, science and information
technology; Creative, leisure and cultural industries; Health and social care.<span>&nbsp; </span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2: Research
entrepreneurship and innovations within a specialist real world setting,
recognising that specialist areas have to be explored at multiple levels of
analysis.<span>&nbsp; </span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3: Apply
core theories, concepts and frameworks of innovation and entrepreneurship to
understand the strategy, process and operations of enterprises at different
stages of their life cycle. A4: Discuss the impact of innovation and
entrepreneurship on society, both at a conceptual and a practical level,
including ethics and sustainability, economic and social benefits to you, the
economy and local communities. <span>&nbsp;</span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: Differentiate the distinctive roles played by start-ups and
established enterprises in the process of developing and commercializing
various forms of innovations. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: Distinguish the responsibilities of founders, managers,
employees and directors within particular types of sustainable enterprises and
innovations, including roles and rewards. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3: Use concepts from enterprise and innovation to critically
analyse and evaluate solutions to a variety of societal challenges. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: Work independently and as part of a collaborative virtual team
to develop attributes and capabilities for entrepreneurial success in a complex
and changing environment. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Undertake independent research to inform practice within your
area of specialism. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3: Critically evaluate and reflect on your own career development
objectives. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Select and apply conceptual thinking for the process of
enterprise development. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2: Critically analyse and design competitive and sustainable
strategies for developing and introducing innovations into particular markets. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D3: Negotiating, influencing, and agreeing roles and rewards
within founder teams in entrepreneurial settings, doing so in a legitimate
ethical manner. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D4: Appropriately plan and solve problems in entrepreneurial and
innovative settings. </span></p>

<span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;font-size:13px;">D5: Deploying effective
networking and persuasive communication skills.</span>&nbsp;<br></td>
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
                    B392&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Advanced Management Accounting <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The module offers students the opportunity to continue their studies in the BA Business Studies after they have completed the B291 &amp; B292 modules. It builds on the knowledge and skills students have learned in B292 by focusing on theories, concepts and techniques at a more advanced level. The learning outcomes also include a critical evaluation of the theories and techniques and their application in ambiguous settings using case study approach. Business entities operate in economic turbulent environments. Under these constraints, decisions taken by managers of business units can vary and differ depending on the manager’s and the company’s pursuit of goals and objectives. Proper economic analysis and use of appropriate techniques and tools are therefore mandatory for managers and decision makers. The module can be used to understand strategy and to situate the role of strategic management accounting within the broader content of organizational and industry differences using theories, tools, techniques and relevant case studies and examples. Basic skills of quantitative proficiency is required in order to understand pricing decisions techniques, financial measures of performance, investments , EVA , Variance analysis , budgeting costing etc. This module provides students with a solid base of Advanced management Accounting study and practice.  
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_16">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_16" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Advanced Management Accounting</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B392</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Advanced Management Accounting</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B292</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>The module offers students the opportunity to continue their studies in the BA Business Studies after they have completed the B291 &amp; B292 modules. It builds on the knowledge and skills students have learned in B292 by focusing on theories, concepts and techniques at a more advanced level. The learning outcomes also include a critical evaluation of the theories and techniques and their application in ambiguous settings using case study approach. Business entities operate in economic turbulent environments. Under these constraints, decisions taken by managers of business units can vary and differ depending on the manager’s and the company’s pursuit of goals and objectives. Proper economic analysis and use of appropriate techniques and tools are therefore mandatory for managers and decision makers. The module can be used to understand strategy and to situate the role of strategic management accounting within the broader content of organizational and industry differences using theories, tools, techniques and relevant case studies and examples. Basic skills of quantitative proficiency is required in order to understand pricing decisions techniques, financial measures of performance, investments , EVA , Variance analysis , budgeting costing etc. This module provides students with a solid base of Advanced management Accounting study and practice.  </td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td>&ZeroWidthSpace;<span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>A. Knowledge
and understanding</strong></span><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1 :
Understand the role of strategic management accounting and apply a strategic
analysis framework in simple complex settings. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2
:Critically select , apply and evaluate management accounting techniques in
strategic costing and pricing including value chain analysis , activity based
costing and business process optimization approaches.<span>&nbsp; </span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3:
Understand, describe and evaluate the sources , costs and risks associated with
the financing of investments. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4: Apply and
critically evaluate advanced techniques for investment appraisal. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A5: Explain,
apply and evaluate methods of accounting control and performance evaluation for
the purpose of improving strategic and operational performance of
organizations. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: Develop the ability to integrate information and use reasoned
approaches to select relevant information and analytical techniques in simple
and complex settings. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: Compare critically and use different approaches to issues and
problems within management accounting. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3: Communicate management accounting information effectively and
appropriately. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B4: Use information and communication technologies appropriately
and effectively.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B5: Use fundamental business mathematics and other quantitative
methods effectively and appropriately</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: Apply digital technologies to analyse data using strategic
management techniques, e.g spread sheets.<span>&nbsp;
</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Frame problems in ambiguous settings independently .Identify
and critically select appropriate information both from digital and print
sources to address these.<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3: Use a combination of electronic applications to communicate
analysis and findings.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C4: Use tools and techniques of management accounting to<span>&nbsp; </span>improve managerial decision making.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Provide students with knowledge and understanding of
management accounting techniques that play an important role in in the
formulation and implementation of business strategy. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2: Examine two key areas of financial management of organizations
and link them to the management accounting and strategic activities of
organizations. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D3: Build on the material already studied by students on
investment appraisal, adding theoretical depth and a critical evaluation of the
techniques.<span>&nbsp; </span></span></p>

<span class="ms-rteFontSize-2" lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D4: Evaluate performance
using benchmarks and appropriate measures of return on investment. </span>&ZeroWidthSpace;<br></td>
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
                    B628&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Managing 1: Organizations and People <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module is designed for managers, aspiring managers, team leaders and supervisors; it uses activities and problem-solving to take you through core topics in organizational behavior and human resource management. Topics include organizational context and culture, stakeholders, management roles, recruitment and induction, performance management, motivation, team work, managing operations and change. These are focused primarily on your own work situations and practices, whether these are in the commercial, public or voluntary sectors.
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
								<span class="modal-title">Managing 1: Organizations and People</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B628</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Managing 1: Organizations and People</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B207B</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module is designed for managers, aspiring managers, team leaders and supervisors; it uses activities and problem-solving to take you through core topics in organizational behavior and human resource management. Topics include organizational context and culture, stakeholders, management roles, recruitment and induction, performance management, motivation, team work, managing operations and change. These are focused primarily on your own work situations and practices, whether these are in the commercial, public or voluntary sectors.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;<span class="ms-rteFontSize-2" id="ms-rterangepaste-start"></span><span class="ms-rteFontSize-2" lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">By the
end of the course students will be enabled to critically reflect on and analyse
workplace situations and their own ways of managing. It is ‘solution oriented’
to help students to not only understand work situations from a manager’s
perspective, but also to help them to work out what to do, given that they may
not be in charge of the organisation they work for. As they work through
activities, problems and solutions, they will question the idea that there are
single solutions or issues or that there is ‘one best way’. they will come to
understand the constraints, choices and demands that operate and learn when to
work within them and when and how they may be able to bring about change.</span>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>A. Knowledge
and understanding</strong></span><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span style="text-decoration:underline;">Module 1 : </span>Managing</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1: the role and context of managerial work with particular
reference to the development of own practice.<span>&nbsp;
</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2: managerial skills ( including problem solving , decision
making, information gathering treatment and presentation) </span></p><p style="text-decoration:underline;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">Module 2:&nbsp; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3: Key processes of people management, incorporating the
recruitment and development of staff and the management and leadership of
individuals, teams and change. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4: Behavioural aspects of the management of leadership of
individuals, teams and change. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span><strong>B. Cognitive skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span>B1:apply management concepts
to work context. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: analyse and critically reflect on work practice and
professional self knowledge. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3: solve management problems through the use of the analytical
skills including problem identification, analysis, logic, thinking and
judgement to the advantage of one's own organization.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: Setting objectives for developing and implementing<span>&nbsp;&nbsp; </span>Operational plans for the area of
responsibility. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Reviewing and evaluating performance and practice.<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3: reflecting and questioning.<span>&nbsp;
</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C4: presenting and reporting information. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C5: problem solving, innovation and decision-making.<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C6: Managing business<span>&nbsp;
</span>processes. <span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Use interpersonal skills including those involved in team
working and collaborating. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2: communicate effectively , using management vocabulary, both
orally and in writing<span>&nbsp; </span>and listen
actively . </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D3: Gather, handle , present and use information effectively;
analyse and evaluate numerical data and information for specific purposes; use
information technologies.<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D4: Demonstrate numeracy and literacy<span>&nbsp; </span></span></p>

<span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;font-size:13px;">D5: Learn how to learn
with an emphasis on self-monitoring and progress towards independent learning.</span>&ZeroWidthSpace;<br></td>
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
                    B629&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Managing 2: Marketing and Finance <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Main elements and realities of a manager’s job and explains how one can develop and organize himself to be effective and successful in his role. Managing in modern organizations is not easy: no context is the same; the ‘right’ decision in one organization may be the ‘wrong’ one in another, or at another time. There is no ‘one best way’. However, there is also ‘received wisdom’ – tried and tested practices and behaviours that are usually effective in bringing about the result a manager wants. These are included in this module where appropriate. But even ‘good practice’ needs adaptation: time or resources may be in short supply and a manager may have to do the best he or she can with what’s available. This is the art of management: doing what’s possible in the best way possible in the circumstances to achieve, through others, the goals for which an organization is striving.
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
								<span class="modal-title">Managing 2: Marketing and Finance</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B629</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Managing 2: Marketing and Finance</td>
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
											<td>Main elements and realities of a manager’s job and explains how one can develop and organize himself to be effective and successful in his role. Managing in modern organizations is not easy: no context is the same; the ‘right’ decision in one organization may be the ‘wrong’ one in another, or at another time. There is no ‘one best way’. However, there is also ‘received wisdom’ – tried and tested practices and behaviours that are usually effective in bringing about the result a manager wants. These are included in this module where appropriate. But even ‘good practice’ needs adaptation: time or resources may be in short supply and a manager may have to do the best he or she can with what’s available. This is the art of management: doing what’s possible in the best way possible in the circumstances to achieve, through others, the goals for which an organization is striving.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p><strong><span style="text-decoration:underline;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;B629-</span></span></strong><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"> Managing 2: Marketing and Finance will cover core topics in
Marketing and Finance.<span>&nbsp; </span>Topics include;
assessing the external environment, consumer relationship, market research,
product/service analysis, price, promotion and delivery, quality, consumer expectations
and satisfaction, financial planning and monitoring through budgets, cash flow,
profit and loss.<span>&nbsp; </span>All these topics will
focus primarily on student’s own work situations and practices. The teaching
and learning strategy of this module is problem-based. Through this approach,
the module aims to develop the skills an effective manager needs: such as
analysis, constructing sound arguments, critical and reflective thinking,
problem identification and solving, active listening and communication, sourcing
and presenting information, and report writing. The course is a management
development vehicle that aims to help student perform more effectively as
managers.<span>&nbsp; </span>It does so by:</span></p><ul><li><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">Increasing student’s foundation management knowledge and competencies </span></li><li><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">Providing a repertoire of theories, concepts, and techniques to apply in different management setting -Helping students understand their individual management role, its context and nature of their interventions in their organizations </span></li><li><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">Encouraging student to be reflective practitioners, applying independent and inquisitive learning in the workplace </span></li><li><span class="ms-rteFontSize-2" lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">Enabling students to understand the discourse of specialist and senior managers better, so that they can hold more confident and informed conversations with them, work more effectively with and where appropriate challenge them. </span></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>A. Knowledge
and understanding</strong></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1: Client
communications, relationships, the role of marketing information and the
development of value. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2: Marketing
planning, service quality with particular reference to own practice. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3:
Understand how financial information can be used to support managerial decision
making (i.e. the relevance of the generation and reporting of financial
information) </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4:
Understand the importance of costs costing and budgeting processes in
managerial decisions A5: Have a good understanding of how business concepts
relate to real life businesses, organizations </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A6:
Importance of performance management for organisations </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span><strong>B. Cognitive skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1. Apply management concepts to work contexts </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2. Analyse and critically reflect on work practice and
professional self-knowledge </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3. Solve management problems through the use of analytical skills
including problem-identification, analysis, logic, critical thinking and
judgment to the advantage of one’s own organization </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B4. Communicate effectively, using management vocabulary, both
orally and in writing and listen actively. Use interpersonal skills including
those involved in team working and collaborating<span>&nbsp;&nbsp;&nbsp;&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B5. Gather, handle, present and use information effectively;
analyse and evaluate numerical data and information for specific purposes; use
information technologies B6. Demonstrate numeracy and literacy and Learn how to
learn with an emphasis on self-monitoring and progress towards independent
learning B7. Critical thinking, analysis and synthesis.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1. Setting objectives for, developing and implementing
operational plans for<span>&nbsp; </span>area of
responsibility<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2. Reviewing and evaluating performance &amp; practice </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3. Reflecting and questioning C4. Presenting and reporting
information </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C5. Problem-solving, innovation and decision-making by using tools
and techniques and models C6. Apply key concepts<span>&nbsp; </span>to managerial decision making the<span>&nbsp; </span>Managing of<span>&nbsp;
</span>business processes&ZeroWidthSpace;</span></p><p><font face="&quot;calibri&quot;,sans-serif"></font><br>&nbsp;</p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1. Use interpersonal skills including those involved in team
working and collaborating<span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2. Communicate effectively, using management vocabulary, both
orally and in writing and listen actively </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D3. Gather, handle, present and use information effectively;
analyse and evaluate numerical data and information for specific purposes; use
information technologies </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D4. Demonstrate numeracy and literacy<span>&nbsp; </span></span></p>

<span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;font-size:13px;">D5. Learn how to learn
with an emphasis on self-monitoring and progress towards independent learning</span>&ZeroWidthSpace;<br></td>
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
                    B863 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Human Resource Professional <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    B863 is a postgraduate course and is one of a series of optional courses offered to all students who progress to Stage II of the AOU MBA program/ mandatory for those who are to specialize This module will consider the role and contribution of the HR professional and the skills needed to be effective in this role. 
Students will consider the implications of recent research findings in the field of human resource management for their own practice, for example in increasing levels of engagement and improving performance, in acting ethically and in managing change. 
They will compare this with the practice of HR professionals in other contexts, drawing on case studies and the experience of their fellow students working in different geographical areas and sectors; and they will also look at the development over time of thinking about the role of HR professionals in order to understand how this may influence current thinking. The emphasis throughout will be on considering what HRM practices are associated with positive organizational outcomes.
Students will develop and practice the skills they will need to be effective as an HR professional, including as a leader and a senior manager. These include self-management, leading and working in teams, making decisions, managing and communicating information, including financial information, consultancy skills and helping others to learn. They will also develop postgraduate study skills and digital literacy skills.
Perhaps most importantly this module will develop students’’ skills as a reflective practitioner, committed to continuously learning from reflection on their practice and on the critical application of new theories and ideas to inform this practice. Collaboration skills of the students with all functional areas of an organization (accounting, human resources, operations, production, marketing, information technology, etc.) will be improved.

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
								<span class="modal-title">The Human Resource Professional</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B863 </td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>The Human Resource Professional</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B870B</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>B863 is a postgraduate course and is one of a series of optional courses offered to all students who progress to Stage II of the AOU MBA program/ mandatory for those who are to specialize This module will consider the role and contribution of the HR professional and the skills needed to be effective in this role. 
Students will consider the implications of recent research findings in the field of human resource management for their own practice, for example in increasing levels of engagement and improving performance, in acting ethically and in managing change. 
They will compare this with the practice of HR professionals in other contexts, drawing on case studies and the experience of their fellow students working in different geographical areas and sectors; and they will also look at the development over time of thinking about the role of HR professionals in order to understand how this may influence current thinking. The emphasis throughout will be on considering what HRM practices are associated with positive organizational outcomes.
Students will develop and practice the skills they will need to be effective as an HR professional, including as a leader and a senior manager. These include self-management, leading and working in teams, making decisions, managing and communicating information, including financial information, consultancy skills and helping others to learn. They will also develop postgraduate study skills and digital literacy skills.
Perhaps most importantly this module will develop students’’ skills as a reflective practitioner, committed to continuously learning from reflection on their practice and on the critical application of new theories and ideas to inform this practice. Collaboration skills of the students with all functional areas of an organization (accounting, human resources, operations, production, marketing, information technology, etc.) will be improved.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p style="text-align:justify;"><span style="font-family:arial, sans-serif;font-size:11pt;">&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;The
primary aims of this course are:</span></p><ul style="margin-top:0in;"><li style="text-align:justify;color:#000000;font-size:11pt;font-style:normal;font-weight:400;"><span style="font-family:arial, sans-serif;font-size:11pt;">To understand the role of the HR professional,
     the nature of professionalism and approaches to<span>&nbsp; </span>addressing ethical dilemmas </span></li><li style="text-align:justify;color:#000000;font-size:11pt;font-style:normal;font-weight:400;"><span style="font-family:arial, sans-serif;font-size:11pt;">To review recent research and to assess its
     relevance for practice in a range of contexts </span></li><li style="text-align:justify;color:#000000;font-size:11pt;font-style:normal;font-weight:400;"><span style="font-family:arial, sans-serif;font-size:11pt;">To assess the relevance of theory for practice
     and apply it where appropriate to improve practice </span></li><li style="text-align:justify;color:#000000;font-size:11pt;font-style:normal;font-weight:400;"><span style="font-family:arial, sans-serif;font-size:11pt;">To review theoretical approaches to leadership
     and team-working and to develop the skills needed to be effective as a leader
     and as a team member </span></li><li style="text-align:justify;color:#000000;font-size:11pt;font-style:normal;font-weight:400;"><span style="font-family:arial, sans-serif;font-size:11pt;">To critically assess the range of concepts and
     issues that are associated with managing performance in the workplace, and
     the interrelationships between these factors&nbsp; </span></li><li style="text-align:justify;color:#000000;font-size:11pt;font-style:normal;font-weight:400;"><span style="font-family:arial, sans-serif;font-size:11pt;">To develop the skills and understanding needed
     to address change management issues and to work at a strategic level in
     the organization </span></li></ul>

<span style="font-family:arial, sans-serif;font-size:11pt;">To develop skills essential for HR work such as:
leading and working in teams, making decisions, managing financial information,
communicating effectively and helping others to learn</span><br></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong>A. Knowledge and understanding</strong></p><p style="text-align:justify;"><strong>A1. </strong>Gain an understanding the theoretical and practical aspects of human resource management to formulate strategies that will enable organizations to achieve both operational and strategic goals related to the organization's human capital.</p><p style="text-align:justify;"><strong>A2.</strong> Define, explain, illustrate and reason with the key role of the HR professional and approaches to addressing ethical dilemmas. </p><p style="text-align:justify;"><strong>A3</strong>. Identify the linkages between HRM functions and operations and performances in the workplace and leadership<br></p><p><strong>B. Cognitive skills</strong></p><p style="text-align:justify;"><strong>B1. </strong>Skills to manage communication initiatives to create and implement human resources initiatives and programs that achieve organizational goals</p><p style="text-align:justify;"><strong>B2</strong><strong>.</strong> Critical thinking and problem-solving skills by assessing and interpreting source materials, evaluating arguments, examining and applying both case-based and real-world business, as consulting teams in the development of business and human resource management solutions<br></p><p><strong><span lang="EN-GB" style="font-family:arial, sans-serif;font-size:11pt;">B3.</span></strong><span lang="EN-GB" style="font-family:arial, sans-serif;font-size:11pt;"> </span><span lang="EN-GB" style="font-family:arial, sans-serif;font-size:11pt;">Collaboration skills with all functional areas
of an organization (accounting, human resources, operations, production,
marketing, information technology, etc.)</span><br><strong>C. Practical and professional skills&nbsp;</strong></p><p style="text-align:justify;"><strong>C1</strong><strong>.</strong> Appraise and apply techniques in talent management that human resource professionals may use to facilitate effective position planning, talent selection, placement, compensation and rewards, as well as retention. </p><p style="text-align:justify;"><strong>C2. </strong>Reflect and comment in a way that demonstrates awareness of the different contexts that impact on the operation of HRM<strong> </strong></p><p style="text-align:justify;"><strong>C3.</strong><strong>&nbsp; </strong>Practice behaviour and performance that demonstrates enhanced competence in HR Skills, leadership, oral and written communication, critical thinking, problem-solving.</p><p><strong>C4.</strong> Recognise the significance of ethical issues in HR practices and the management of people in the workplace.<br></p><p><strong>D Key transferable skills&nbsp;</strong></p><p style="text-align:justify;margin-bottom:6pt;"><strong><span style="font-family:arial, sans-serif;font-size:11pt;">D1.</span></strong><span style="font-family:arial, sans-serif;font-size:11pt;">
Gain s</span><span lang="EN-GB" style="font-family:arial, sans-serif;font-size:11pt;">kills necessary to work effectively in teams,
assuming roles of leader and follower</span></p><p style="text-align:justify;margin-bottom:6pt;"><strong><span style="font-family:arial, sans-serif;font-size:11pt;">D2. </span></strong><span lang="EN-GB" style="font-family:arial, sans-serif;font-size:11pt;">Learn through
reflection on practice and experience.</span></p><p style="text-align:justify;margin-bottom:6pt;"><strong><span style="font-family:arial, sans-serif;font-size:11pt;">D3. </span></strong><span lang="EN-GB" style="font-family:arial, sans-serif;font-size:11pt;">Demonstrate people management skills
essential for HR work such as: selection interviewing; appraisal interviewing;
disciplinary interviewing; delivering training; making presentations; project
management; managing performance</span></p><p style="text-align:justify;margin-bottom:6pt;"><strong><span lang="EN-GB" style="font-family:arial, sans-serif;font-size:11pt;">D4.</span></strong><span lang="EN-GB" style="font-family:arial, sans-serif;font-size:11pt;"><span>&nbsp;
</span></span><span lang="EN-GB" style="font-family:arial, sans-serif;font-size:11pt;">Gain proficiency in communication skills,
independent action and team working.</span><span lang="EN-GB" style="font-family:arial, sans-serif;font-size:11pt;"></span></p><p style="text-align:justify;margin-bottom:6pt;"><strong><span lang="EN-GB" style="font-family:arial, sans-serif;font-size:11pt;">D5.</span></strong><span lang="EN-GB" style="font-family:arial, sans-serif;font-size:11pt;"> Manage and
communicate information using IT applications and software packages in
accordance with the requirements of the Digital Information Literacy Levels
Framework.<span>&nbsp; </span></span><span lang="EN-GB" style="font-family:arial, sans-serif;font-size:11pt;">&ZeroWidthSpace;</span></p>

<p><br>&nbsp;</p></td>
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
                    B870A&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Managing in a changing world-Management <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The module provides you with the opportunity to develop and learn about managing and marketing in relation to your working life and personal practice. As an aspiring organisational decision-maker, you'll gain the knowledge and tools necessary to successfully take advantage of cutting-edge theories of management and human resource management. This will be linked to the values of collective responsibility, aesthetics and ethics. You'll become empowered to create responsible growth, across a range of private sector, public and not for profit organisations, while also critically reflecting on your own potential in terms of leadership and management practice. In addition, you'll explores the ways in which marketing can be used to more effectively help organisations to be both successful and forward thinking in a business environment that is quickly moving beyond traditional geographic, cultural and organisational boundaries. The module offers a developmental route appropriate for the first module of an MBA, which builds on and consolidates knowledge through a series of activities and text.
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
								<span class="modal-title">Managing in a changing world-Management</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B870A</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Managing in a changing world-Management</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>The module provides you with the opportunity to develop and learn about managing and marketing in relation to your working life and personal practice. As an aspiring organisational decision-maker, you'll gain the knowledge and tools necessary to successfully take advantage of cutting-edge theories of management and human resource management. This will be linked to the values of collective responsibility, aesthetics and ethics. You'll become empowered to create responsible growth, across a range of private sector, public and not for profit organisations, while also critically reflecting on your own potential in terms of leadership and management practice. In addition, you'll explores the ways in which marketing can be used to more effectively help organisations to be both successful and forward thinking in a business environment that is quickly moving beyond traditional geographic, cultural and organisational boundaries. The module offers a developmental route appropriate for the first module of an MBA, which builds on and consolidates knowledge through a series of activities and text.</td>
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
                    B870B&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Managing in a changing world-Marketing <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    B870 Part B Managing in a changing world. While studying this module, you will be encouraged to develop, as well as challenge, your current knowledge and skills in order to meet the contemporary and rapidly changing areas of management, marketing, ethics and leadership. Using both independent and collaborative approaches to learning, this module will enable you to integrate and understand ways of managing these core business functions in the face of globalisation, technological advancements and other recent economic, social and political challenges. B 870 B Theme provides a coherent and strong conceptual narrative to the module. These overarching themes provide a way of relating different and disparate knowledge to a conceptually organised framework. The theme consists of, Unitarism and Pluralism, challenges the idea that there is one best way and the assumption that when we speak of ‘an organisation’ we are talking about one harmonious and homogenous entity.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_105">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_105" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Managing in a changing world-Marketing</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B870B</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Managing in a changing world-Marketing</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B870A</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>B870 Part B Managing in a changing world. While studying this module, you will be encouraged to develop, as well as challenge, your current knowledge and skills in order to meet the contemporary and rapidly changing areas of management, marketing, ethics and leadership. Using both independent and collaborative approaches to learning, this module will enable you to integrate and understand ways of managing these core business functions in the face of globalisation, technological advancements and other recent economic, social and political challenges. B 870 B Theme provides a coherent and strong conceptual narrative to the module. These overarching themes provide a way of relating different and disparate knowledge to a conceptually organised framework. The theme consists of, Unitarism and Pluralism, challenges the idea that there is one best way and the assumption that when we speak of ‘an organisation’ we are talking about one harmonious and homogenous entity.</td>
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
                    B872&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creating and sustaining value-Financial Management <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This course is an elective for the direct entrants to the Finance track of the MBA programme. The scope of this course relates to the central managerial aspects of understanding, creating, improving and sustaining value within contemporary organisations. This course will enable the participant to gain a greater understanding of how decisions and organisational performance can be optimised. This module will help you understand how different business functions, such as management accounting, financial reporting, operations management and business intelligence, contribute to sustainable value creation. Most importantly, the module moves beyond a treatment of functional areas, towards a systemic view of organisational functions. Through this systemic view, you will be able to expand your critical understanding of what constitutes organisational value and how a range of value perspectives can be implemented within diverse organisational contexts. By the end of this module, you should have a greater understanding of what creating and sustaining value is and be more confident in applying these ideas in your daily work life.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_106">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_106" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Creating and sustaining value-Financial Management</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B872</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Creating and sustaining value-Financial Management</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This course is an elective for the direct entrants to the Finance track of the MBA programme. The scope of this course relates to the central managerial aspects of understanding, creating, improving and sustaining value within contemporary organisations. This course will enable the participant to gain a greater understanding of how decisions and organisational performance can be optimised. This module will help you understand how different business functions, such as management accounting, financial reporting, operations management and business intelligence, contribute to sustainable value creation. Most importantly, the module moves beyond a treatment of functional areas, towards a systemic view of organisational functions. Through this systemic view, you will be able to expand your critical understanding of what constitutes organisational value and how a range of value perspectives can be implemented within diverse organisational contexts. By the end of this module, you should have a greater understanding of what creating and sustaining value is and be more confident in applying these ideas in your daily work life.</td>
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
                    B873&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Effective Strategic management <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module B873 Effective strategic management in business and the public sector will provide the student with the necessary tools to become an effective strategic decision-maker. Students will learn about the strategic analysis of the organizational environment, strategic decision-making processes, and the implementation of preferred strategic choices. The module will also support the development of soft skills, which student will require both to progress in the qualification and succeed in the workplace by applying their learning to their own context. By the end of this module, student should have a greater understanding of what strategic management is and be able to apply their learning to your own workplace. This module intends to provide student's ways of increasing levels of engagement and improving performance, in acting ethically and in managing change. This module draws on case studies and the experience of their fellow students working in different geographical areas and sectors; and they will also look at the development over time of thinking about the role of strategy in order to understand how this may influence current thinking. The emphasis throughout will be on considering what Strategy practices are associated with positive organizational outcomes. Students will develop and practice the skills they will need to be effective as a Strategist, including as a leader and a senior manager. These include self-management, leading and working in teams, making decisions, managing and communicating information, including financial information, consultancy skills and helping others to learn. They will also develop postgraduate study skills and digital literacy skills. Most importantly this module will develop students’’ skills as a reflective practitioner, committed to continuously learning from reflection on their practice and on the critical application of new theories and ideas to inform this practice.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_108">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_108" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Effective Strategic management</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B873</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Effective Strategic management</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B870A</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module B873 Effective strategic management in business and the public sector will provide the student with the necessary tools to become an effective strategic decision-maker. Students will learn about the strategic analysis of the organizational environment, strategic decision-making processes, and the implementation of preferred strategic choices. The module will also support the development of soft skills, which student will require both to progress in the qualification and succeed in the workplace by applying their learning to their own context. By the end of this module, student should have a greater understanding of what strategic management is and be able to apply their learning to your own workplace. This module intends to provide student's ways of increasing levels of engagement and improving performance, in acting ethically and in managing change. This module draws on case studies and the experience of their fellow students working in different geographical areas and sectors; and they will also look at the development over time of thinking about the role of strategy in order to understand how this may influence current thinking. The emphasis throughout will be on considering what Strategy practices are associated with positive organizational outcomes. Students will develop and practice the skills they will need to be effective as a Strategist, including as a leader and a senior manager. These include self-management, leading and working in teams, making decisions, managing and communicating information, including financial information, consultancy skills and helping others to learn. They will also develop postgraduate study skills and digital literacy skills. Most importantly this module will develop students’’ skills as a reflective practitioner, committed to continuously learning from reflection on their practice and on the critical application of new theories and ideas to inform this practice.</td>
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
                    B874&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Finance for strategic decision making <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module will provide you with the necessary tools to use financial information and other data for making management decisions. You will learn a range of accounting and data analysis techniques as well as being introduced to the workings of the financial markets. Additionally, the module will make use of Excel spreadsheets and discuss good spreadsheet practice. The module is designed for professionals from a wide range of contexts and backgrounds who need to actively to engage with the challenges of using financial and other quantitative information for making decisions.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_109">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_109" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Finance for strategic decision making</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B874</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Finance for strategic decision making</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>Co-requisite B872</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module will provide you with the necessary tools to use financial information and other data for making management decisions. You will learn a range of accounting and data analysis techniques as well as being introduced to the workings of the financial markets. Additionally, the module will make use of Excel spreadsheets and discuss good spreadsheet practice. The module is designed for professionals from a wide range of contexts and backgrounds who need to actively to engage with the challenges of using financial and other quantitative information for making decisions.</td>
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
                    B875&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MBA project: leaders of change (Capstone) <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module will build specialized expertise by putting the theory and central managerial aspects taught on the MBA into practice, engaging in a life-changing learning that can challenge students understanding of theories and management practices. Students will identify a real problem in an organization and look for a change that will help solve this problem. This will enable students to develop as leaders of change that go beyond mere applications of theoretical and practical skills to be reflective practitioners, critical thinkers, and independent professionals. In this module students study contemporary aspects of management and industry in depth, carry out high level research, utilize data, evaluate literature, and present their findings accurately and concisely.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_110">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_110" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">MBA project: leaders of change (Capstone)</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>B875</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>MBA project: leaders of change (Capstone)</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B874&amp;B873</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module will build specialized expertise by putting the theory and central managerial aspects taught on the MBA into practice, engaging in a life-changing learning that can challenge students understanding of theories and management practices. Students will identify a real problem in an organization and look for a change that will help solve this problem. This will enable students to develop as leaders of change that go beyond mere applications of theoretical and practical skills to be reflective practitioners, critical thinkers, and independent professionals. In this module students study contemporary aspects of management and industry in depth, carry out high level research, utilize data, evaluate literature, and present their findings accurately and concisely.</td>
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
                    BA100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Career Planning and Development <span class="float-right">(1) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This course aims at making students aware of the need for career planning and self-developmental activities. It teaches the effective ways of developing curriculum vitae and the cover letter for applying for a job. It will teach the various techniques that students can use to develop the communication skills in particular the written communication skills. By studying this course, students get familiarized with the various job search methods and the effective utilization of such job search methods. This will make students understand the importance of concept of career planning and make them to think about the ways and means of achieving those plans.
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
								<span class="modal-title">Career Planning and Development</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>BA100</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Career Planning and Development</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>EL111</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>1</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This course aims at making students aware of the need for career planning and self-developmental activities. It teaches the effective ways of developing curriculum vitae and the cover letter for applying for a job. It will teach the various techniques that students can use to develop the communication skills in particular the written communication skills. By studying this course, students get familiarized with the various job search methods and the effective utilization of such job search methods. This will make students understand the importance of concept of career planning and make them to think about the ways and means of achieving those plans.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;<br></p><p style="box-sizing:border-box;margin-bottom:1rem;color:#212529;font-family:&quot;alegreya sans&quot;, &quot;droid kufi&quot;, sans-serif;font-size:16px;background-color:#ffffff;"><span class="ms-rteFontSize-2" style="box-sizing:border-box;">&ZeroWidthSpace;<span style="box-sizing:border-box;line-height:16.8667px;color:black;top:0.5pt;letter-spacing:-0.05pt;"><span style="box-sizing:border-box;">T</span></span><span style="box-sizing:border-box;line-height:16.8667px;color:black;top:0.5pt;"><span style="box-sizing:border-box;">he</span><span style="box-sizing:border-box;letter-spacing:0.45pt;">&nbsp;</span><span style="box-sizing:border-box;">o</span><span style="box-sizing:border-box;letter-spacing:-0.05pt;"><span style="box-sizing:border-box;">v</span></span><span style="box-sizing:border-box;">erall</span><span style="box-sizing:border-box;letter-spacing:0.55pt;">&nbsp;</span><span style="box-sizing:border-box;letter-spacing:-0.05pt;"><span style="box-sizing:border-box;">g</span></span><span style="box-sizing:border-box;">oal</span><span style="box-sizing:border-box;letter-spacing:0.45pt;">&nbsp;</span><span style="box-sizing:border-box;letter-spacing:0.1pt;"><span style="box-sizing:border-box;">o</span></span><span style="box-sizing:border-box;">f</span><span style="box-sizing:border-box;letter-spacing:0.45pt;">&nbsp;</span><span style="box-sizing:border-box;">the</span><span style="box-sizing:border-box;letter-spacing:0.6pt;">&nbsp;</span><span style="box-sizing:border-box;">co</span><span style="box-sizing:border-box;letter-spacing:-0.05pt;"><span style="box-sizing:border-box;">ur</span></span><span style="box-sizing:border-box;">se</span><span style="box-sizing:border-box;letter-spacing:0.5pt;">&nbsp;</span><span style="box-sizing:border-box;">is</span><span style="box-sizing:border-box;letter-spacing:0.5pt;">&nbsp;</span><span style="box-sizing:border-box;">to</span><span style="box-sizing:border-box;letter-spacing:0.5pt;">&nbsp;</span><span style="box-sizing:border-box;">ma</span><span style="box-sizing:border-box;letter-spacing:-0.05pt;"><span style="box-sizing:border-box;">k</span></span><span style="box-sizing:border-box;">e</span><span style="box-sizing:border-box;letter-spacing:0.5pt;">&nbsp;</span><span style="box-sizing:border-box;">the</span><span style="box-sizing:border-box;letter-spacing:0.6pt;">&nbsp;</span><span style="box-sizing:border-box;">stu</span><span style="box-sizing:border-box;letter-spacing:-0.05pt;"><span style="box-sizing:border-box;">d</span></span><span style="box-sizing:border-box;letter-spacing:0.2pt;"><span style="box-sizing:border-box;">e</span></span><span style="box-sizing:border-box;">n</span><span style="box-sizing:border-box;letter-spacing:0.05pt;"><span style="box-sizing:border-box;">t</span></span><span style="box-sizing:border-box;">s</span><span style="box-sizing:border-box;letter-spacing:0.45pt;">&nbsp;</span><span style="box-sizing:border-box;letter-spacing:-0.05pt;"><span style="box-sizing:border-box;">f</span></span><span style="box-sizing:border-box;">amiliar</span><span style="box-sizing:border-box;letter-spacing:0.45pt;">&nbsp;</span><span style="box-sizing:border-box;letter-spacing:-0.05pt;"><span style="box-sizing:border-box;">w</span></span><span style="box-sizing:border-box;">i</span><span style="box-sizing:border-box;letter-spacing:0.05pt;"><span style="box-sizing:border-box;">t</span></span><span style="box-sizing:border-box;">h</span><span style="box-sizing:border-box;letter-spacing:0.45pt;">&nbsp;</span><span style="box-sizing:border-box;">t</span><span style="box-sizing:border-box;letter-spacing:0.1pt;"><span style="box-sizing:border-box;">h</span></span><span style="box-sizing:border-box;">e</span><span style="box-sizing:border-box;letter-spacing:0.5pt;">&nbsp;</span><span style="box-sizing:border-box;">conce</span><span style="box-sizing:border-box;letter-spacing:0.05pt;"><span style="box-sizing:border-box;">p</span></span><span style="box-sizing:border-box;">ts</span><span style="box-sizing:border-box;letter-spacing:0.5pt;">&nbsp;</span><span style="box-sizing:border-box;">li</span><span style="box-sizing:border-box;letter-spacing:-0.05pt;"><span style="box-sizing:border-box;">k</span></span><span style="box-sizing:border-box;">e</span><span style="box-sizing:border-box;letter-spacing:0.5pt;">&nbsp;</span><span style="box-sizing:border-box;">ca</span><span style="box-sizing:border-box;letter-spacing:-0.05pt;"><span style="box-sizing:border-box;">r</span></span><span style="box-sizing:border-box;">e</span><span style="box-sizing:border-box;letter-spacing:0.05pt;"><span style="box-sizing:border-box;">er&nbsp;</span></span></span>&ZeroWidthSpace;<span style="box-sizing:border-box;text-align:justify;"><span style="box-sizing:border-box;">planning and development and with the job search methods. &nbsp;Students also get to know the art of developing curriculum vitae and cover letter to apply for jobs.</span></span></span></p><p style="box-sizing:border-box;margin-bottom:1rem;color:#212529;font-family:&quot;alegreya sans&quot;, &quot;droid kufi&quot;, sans-serif;font-size:16px;background-color:#ffffff;text-align:justify;"><span class="ms-rteFontSize-2" style="box-sizing:border-box;">The &nbsp;main &nbsp;objective &nbsp;of &nbsp;this &nbsp;course &nbsp;is &nbsp;to &nbsp;develop &nbsp;the &nbsp;skills &nbsp;of &nbsp;students &nbsp;in &nbsp;the &nbsp;areas &nbsp;like developing effective curriculum vitae, facing interviews, planning for further moves in their career.</span></p><p style="box-sizing:border-box;margin-bottom:1rem;color:#212529;font-family:&quot;alegreya sans&quot;, &quot;droid kufi&quot;, sans-serif;font-size:16px;background-color:#ffffff;"><span class="ms-rteFontSize-2" style="box-sizing:border-box;">Students need to plan their career in their life to progress. Progression in career needs careful planning. This course will teach on developing career plans and implementing them. It teaches certain techniques that can be used by the students to win over the competition in the job market as well to excel in their care</span>er&ZeroWidthSpace;<br><br></p><p>&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;</p><p style="box-sizing:border-box;margin-bottom:1rem;color:#212529;font-family:&quot;alegreya sans&quot;, &quot;droid kufi&quot;, sans-serif;font-size:16px;">The following are the learning outcomes of the course:<br style="box-sizing:border-box;">1.&nbsp; &nbsp;Developing curriculum vitae and a cover letter for a job on their own.<br style="box-sizing:border-box;">2.&nbsp; &nbsp;Acquiring the necessary skills of creating and sustaining network and relationship with people and organizations.<br style="box-sizing:border-box;">3.&nbsp; &nbsp;Making career plans and learning the ways and means of implementing the career<br style="box-sizing:border-box;">plans.<br style="box-sizing:border-box;">4.&nbsp; &nbsp;Learn and understand various job search methods available with its pros and cons.</p><p style="box-sizing:border-box;margin-bottom:1rem;color:#212529;font-family:&quot;alegreya sans&quot;, &quot;droid kufi&quot;, sans-serif;font-size:16px;">5.&nbsp; &nbsp;(e) Improving the oral and written communication skills.&ZeroWidthSpace;<br><br></p><p><br></p></td>
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
                    BB848&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Leadership and management intercultural context <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    "This course is relevant to any managerial career. It has particular relevance if you are considering or already have an international career or if your managerial and leadership role involves interaction with or within intercultural or intracultural organisations or contexts. Given the increasingly intercultural and globally connected nature of business, management and organisations, this course provides opportunities for you to question and reflect on your own practice and to develop ways of managing and leading which are appropriate in different national and regional settings. By offering new (cross-national) perspectives on leadership and management you are also challenged to rethink your own practices in your current setting. This course addresses issues facing managers and leaders working in intercultural contexts and supports you to develop skills, competencies and knowledge to thrive and to get the best from colleagues, partners and associates. The course covers three main themes: Theme One: Understanding cultures effects: This theme explores different approaches to understanding cultures. Theme Two: Understanding the role of social, political and economic institutions: Drawing on a varieties of capitalism approach, this section looks at the ways in which institutions such as labour markets, forms of firm governance, legal systems, differences in the rule of law, and the structure of inter-firm collaboration and competition affect the practices and challenges of leadership and management. Activities encourage you to explore the ways in which the business, social, economic and political environments affect your own experience of leadership and management. Theme Three: Putting it into practice: cross-cultural leadership capabilities: This theme explores the implications of what you have learned for your own practice and uses, with a series of self-assessment tools to evaluate and assess your own strengths and development needs in relation to the challenges of intercultural leadership and management. This course is relevant to any managerial career. It has particular relevance if you are considering or already have an international career or if your managerial and leadership role involves interaction with or within intercultural or intracultural organisations or contexts. Given the increasingly intercultural and globally connected nature of business, management and organisations, this course provides opportunities for you to question and reflect on your own practice and to develop ways of managing and leading which are appropriate in different national and regional settings. By offering new (cross-national) perspectives on leadership and management you are also challenged to rethink your own practices in your current setting. This course addresses issues facing managers and leaders working in intercultural contexts and supports you to develop skills, competencies and knowledge to thrive and to get the best from colleagues, partners and associates. The course covers three main themes: Theme One: Understanding cultures effects: This theme explores different approaches to understanding cultures. Theme Two: Understanding the role of social, political and economic institutions: Drawing on a varieties of capitalism approach, this section looks at the ways in which institutions such as labour markets, forms of firm governance, legal systems, differences in the rule of law, and the structure of inter-firm collaboration and competition affect the practices and challenges of leadership and management. Activities encourage you to explore the ways in which the business, social, economic and political environments affect your own experience of leadership and management. Theme Three: Putting it into practice: cross-cultural leadership capabilities: This theme explores the implications of what you have learned for your own practice and uses, with a series of self-assessment tools to evaluate and assess your own strengths and development needs in relation to the challenges of intercultural leadership and management. "
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_111">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_111" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Leadership and management intercultural context</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>BB848</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Leadership and management intercultural context</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>"This course is relevant to any managerial career. It has particular relevance if you are considering or already have an international career or if your managerial and leadership role involves interaction with or within intercultural or intracultural organisations or contexts. Given the increasingly intercultural and globally connected nature of business, management and organisations, this course provides opportunities for you to question and reflect on your own practice and to develop ways of managing and leading which are appropriate in different national and regional settings. By offering new (cross-national) perspectives on leadership and management you are also challenged to rethink your own practices in your current setting. This course addresses issues facing managers and leaders working in intercultural contexts and supports you to develop skills, competencies and knowledge to thrive and to get the best from colleagues, partners and associates. The course covers three main themes: Theme One: Understanding cultures effects: This theme explores different approaches to understanding cultures. Theme Two: Understanding the role of social, political and economic institutions: Drawing on a varieties of capitalism approach, this section looks at the ways in which institutions such as labour markets, forms of firm governance, legal systems, differences in the rule of law, and the structure of inter-firm collaboration and competition affect the practices and challenges of leadership and management. Activities encourage you to explore the ways in which the business, social, economic and political environments affect your own experience of leadership and management. Theme Three: Putting it into practice: cross-cultural leadership capabilities: This theme explores the implications of what you have learned for your own practice and uses, with a series of self-assessment tools to evaluate and assess your own strengths and development needs in relation to the challenges of intercultural leadership and management. This course is relevant to any managerial career. It has particular relevance if you are considering or already have an international career or if your managerial and leadership role involves interaction with or within intercultural or intracultural organisations or contexts. Given the increasingly intercultural and globally connected nature of business, management and organisations, this course provides opportunities for you to question and reflect on your own practice and to develop ways of managing and leading which are appropriate in different national and regional settings. By offering new (cross-national) perspectives on leadership and management you are also challenged to rethink your own practices in your current setting. This course addresses issues facing managers and leaders working in intercultural contexts and supports you to develop skills, competencies and knowledge to thrive and to get the best from colleagues, partners and associates. The course covers three main themes: Theme One: Understanding cultures effects: This theme explores different approaches to understanding cultures. Theme Two: Understanding the role of social, political and economic institutions: Drawing on a varieties of capitalism approach, this section looks at the ways in which institutions such as labour markets, forms of firm governance, legal systems, differences in the rule of law, and the structure of inter-firm collaboration and competition affect the practices and challenges of leadership and management. Activities encourage you to explore the ways in which the business, social, economic and political environments affect your own experience of leadership and management. Theme Three: Putting it into practice: cross-cultural leadership capabilities: This theme explores the implications of what you have learned for your own practice and uses, with a series of self-assessment tools to evaluate and assess your own strengths and development needs in relation to the challenges of intercultural leadership and management. "</td>
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
                    BB849&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Supply chain management <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    تم تصميم هذا المقرر للذين يرغبون في معرفة جيدة ورؤية ثاقبة لإدارة سلسلة التوريد وسوف تروق لكل من محترفي سلسلة التوريد والمديرين في المهن الأخرى. سيوفر لك هذا المقرر نظرة معمقة حول النظرية والمشكلات والحلول وأفضل الممارسات في مجال إدارة سلسلة التوريد. سيوفر لك فرصًا للتساؤل والتفكير في مؤسستك ودورها في سلسلة التوريد الأوسع. سيساعدك أيضًا على تطوير قدرتك على تحديد فرص تحسين تصميم المنتج ومعالجات التصنيع واستراتيجيات التوريد وتطوير السوق.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_107">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_107" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Supply chain management</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>BB849</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Supply chain management</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>تم تصميم هذا المقرر للذين يرغبون في معرفة جيدة ورؤية ثاقبة لإدارة سلسلة التوريد وسوف تروق لكل من محترفي سلسلة التوريد والمديرين في المهن الأخرى. سيوفر لك هذا المقرر نظرة معمقة حول النظرية والمشكلات والحلول وأفضل الممارسات في مجال إدارة سلسلة التوريد. سيوفر لك فرصًا للتساؤل والتفكير في مؤسستك ودورها في سلسلة التوريد الأوسع. سيساعدك أيضًا على تطوير قدرتك على تحديد فرص تحسين تصميم المنتج ومعالجات التصنيع واستراتيجيات التوريد وتطوير السوق.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p><br><br></p></td>
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
                    BB851&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Entrepreneurship in context <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module aims to equip you with an entrepreneurial mindset that helps you to make better career decisions – either in your workplace or as an independent entrepreneur – and effectively cope with the increasingly rapid changes in economy and society. In this module, entrepreneurship is broadly described as the application of enterprise behaviors with the aim to create economic, social, environmental, or cultural value in various contexts, among them private and public organizations, small enterprises, large corporations. Specifically, it goes beyond new venture creation (i.e. entrepreneurship) and considers the application of entrepreneurial skills and knowledge in established organizations (i.e. intrapreneurship) to initiate innovation, change and organizational development. Therefore, you need not aim to start your own venture to enjoy studying this module.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_112">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_112" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Entrepreneurship in context</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>BB851</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Entrepreneurship in context</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module aims to equip you with an entrepreneurial mindset that helps you to make better career decisions – either in your workplace or as an independent entrepreneur – and effectively cope with the increasingly rapid changes in economy and society. In this module, entrepreneurship is broadly described as the application of enterprise behaviors with the aim to create economic, social, environmental, or cultural value in various contexts, among them private and public organizations, small enterprises, large corporations. Specifically, it goes beyond new venture creation (i.e. entrepreneurship) and considers the application of entrepreneurial skills and knowledge in established organizations (i.e. intrapreneurship) to initiate innovation, change and organizational development. Therefore, you need not aim to start your own venture to enjoy studying this module.</td>
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
                    BDE850&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Digital Economy in Business <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This module consolidates, integrates, and assesses your learning from the Digital Economy. The Digital Economy explains the new economy, the new enterprise, and the new technology, and how they link to one another, how they enable one another. If you and your organization understand these relationships, the role of the new technology in creating the new enterprise for a new economy, you can be successful.
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_113">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_113" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Digital Economy in Business</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>BDE850</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Digital Economy in Business</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td></td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This module consolidates, integrates, and assesses your learning from the Digital Economy. The Digital Economy explains the new economy, the new enterprise, and the new technology, and how they link to one another, how they enable one another. If you and your organization understand these relationships, the role of the new technology in creating the new enterprise for a new economy, you can be successful.</td>
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
                    BUS101&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Introduction to Math for Business <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The world is a small place these days with business becoming more and more of a global endeavour. This course, Introduction to Math for Business aim to equip students with technical skills and business knowledge needed for further advanced courses in finance. Students need to have effective financial skills for both their personal and professional lives.
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
								<span class="modal-title">Introduction to Math for Business</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>BUS101</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Introduction to Math for Business</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>EL099 </td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>The world is a small place these days with business becoming more and more of a global endeavour. This course, Introduction to Math for Business aim to equip students with technical skills and business knowledge needed for further advanced courses in finance. Students need to have effective financial skills for both their personal and professional lives.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p style="text-align:left;"><span class="ms-rteFontFace-13" lang="EN-GB" style="font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">&ZeroWidthSpace;&ZeroWidthSpace;The overall aims of
this course are to introduce entry knowledge of finance and to provide the
computational skills needed for evaluating financial decisions. Thus providing
learners a footstep into the world of Business Mathematics. This introductory
module introduces learners to the mathematical concepts, vocabulary, and
terminology employed nowadays in the business world in Finance, Banking, and
Accounting to name a few.</span></p><p style="text-align:left;"><span class="ms-rteFontFace-13" lang="EN-GB" style="font-size:11pt;">More specifically, the
students will gain practical experience into aspects such as percentages,
discounts, markups and markdowns, payroll, interest calculations, installment
buying, and annuities.</span><span lang="EN-GB" style="font-family:&quot;times new roman&quot;,serif;font-size:12pt;"> </span></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span lang="EN-GB" style="font-family:&quot;arial&quot;,sans-serif;font-size:11pt;"><strong>A. Knowledge
and understanding</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">A1: Knowledge
and understanding of the depth of relation between math and business
(particularly finance)</span></p><p><span lang="EN-GB" style="font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">A2: Knowledge
and understanding of a range of ideas concerning basic business mathematics and
its applications. </span></p><p><span lang="EN-GB" style="font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">A3: Knowledge
and understanding of relevant ideas, tools, and techniques that are widely used
in everyday business practice.</span></p><p align="right" dir="RTL" style="text-align:left;"><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;"><strong>B. Cognitive skills</strong></span></p><p align="right" dir="RTL" style="text-align:left;"></p><div dir="ltr" style="padding:0px;text-align:left;margin-top:0px;margin-right:0px;margin-bottom:0px;"><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;">B1: the ability to develop skills in interpreting and explaining mathematics</span><span dir="RTL"></span><span dir="RTL"></span><span lang="AR-SA" style="color:black;font-family:&quot;arial&quot;,sans-serif;"><span dir="RTL"></span><span dir="RTL"></span>.</span><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;"></span></div><div style="padding:0px;text-align:left;margin-top:0px;margin-right:0px;margin-bottom:0px;"><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;">&nbsp;</span></div><div style="padding:0px;text-align:left;margin-top:0px;margin-right:0px;margin-bottom:0px;"><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;">B2: the ability to integrate mathematical ideas into everyday thinking</span><span dir="RTL"></span><span dir="RTL"></span><span lang="AR-SA" style="color:black;font-family:&quot;arial&quot;,sans-serif;"><span dir="RTL"></span><span dir="RTL"></span>.</span><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;"></span></div><div style="padding:0px;text-align:left;margin-top:0px;margin-right:0px;margin-bottom:0px;"><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;">&nbsp;</span></div><div style="padding:0px;text-align:left;margin-top:0px;margin-right:0px;margin-bottom:0px;"><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;">B3: the ability to develop mathematical modeling skills</span><span dir="RTL"></span><span dir="RTL"></span><span lang="AR-SA" style="color:black;font-family:&quot;arial&quot;,sans-serif;"><span dir="RTL"></span><span dir="RTL"></span>.</span><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;"></span></div><div style="padding:0px;text-align:left;margin-top:0px;margin-right:0px;margin-bottom:0px;"><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;">&nbsp;</span></div><div style="padding:0px;text-align:left;margin-top:0px;margin-right:0px;margin-bottom:0px;"><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;">B4: the ability to develop basic mathematical financial skills</span><span dir="RTL"></span><span dir="RTL"></span><span lang="AR-SA" style="color:black;font-family:&quot;arial&quot;,sans-serif;"><span dir="RTL"></span><span dir="RTL"></span>.</span><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;"></span></div><div style="padding:0px;text-align:left;margin-top:0px;margin-right:0px;margin-bottom:0px;"><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;">&nbsp;</span></div><div style="padding:0px;text-align:left;margin-top:0px;margin-right:0px;margin-bottom:0px;"><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;">B5: the ability to use techniques from the course to analyse and solve problems in a range of contexts</span><span dir="RTL"></span><span dir="RTL"></span><span lang="AR-SA" style="color:black;font-family:&quot;arial&quot;,sans-serif;"><span dir="RTL"></span><span dir="RTL"></span>.</span><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;"></span></div><div style="padding:0px;text-align:left;margin-top:0px;margin-right:0px;margin-bottom:0px;"><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;">&nbsp;</span></div><div style="padding:0px;text-align:left;margin-top:0px;margin-right:0px;margin-bottom:0px;"><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;">B6: the ability to recognize, interpret and criticize the use of mathematics in different contexts</span><span dir="RTL"></span><span dir="RTL"></span><span lang="AR-SA" style="color:black;font-family:&quot;arial&quot;,sans-serif;"><span dir="RTL"></span><span dir="RTL"></span>.</span><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;"></span></div><div style="padding:0px;text-align:left;margin-top:0px;margin-right:0px;margin-bottom:0px;"><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;">&nbsp;</span></div><div style="padding:0px;text-align:left;margin-top:0px;margin-right:0px;margin-bottom:0px;"><span lang="EN-GB" dir="LTR" style="color:black;font-family:&quot;arial&quot;,sans-serif;">B7: the ability to reason logically using mathematical ideas and principles of the course</span><span dir="RTL"></span><span dir="RTL"></span><span lang="AR-SA" style="color:black;font-family:&quot;arial&quot;,sans-serif;"><span dir="RTL"></span><span dir="RTL"></span>.</span><span lang="EN-GB" style="font-family:&quot;arial&quot;,sans-serif;font-size:11pt;"><br></span></div><span lang="EN-GB" style="font-family:&quot;arial&quot;,sans-serif;font-size:11pt;"><p style="text-align:left;"><br>&nbsp;</p><p><span lang="EN-GB" style="font-size:13px;"><strong>C. Practical and professional skills</strong>&ZeroWidthSpace;</span></p><p><span lang="EN-GB">C1: practically deal with numbers and
manipulate them confidently.</span></p><p><span lang="EN-GB">C2: easily use a calculator and its
functions.</span></p>

<span class="ms-rteFontFace-13" lang="EN-GB">C3: master the techniques of discounts,
mark-ups/markdowns, payroll, credit consumer, simple &amp; compounded
interests, and annuities.</span></span><br></td>
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
                    BUS102&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Introduction to Statistics <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The course helps students understand the relationship between statistics and the world, bringing life to the theory and methods. It incorporates an unprecedented amount of real and interesting data that will help students to connect statistics to their daily lives.

BUS102 is considered an introductory course for BUS202 (data analysis). At the undergraduate level, both modules (BUS102 and BUS202) are considered as part of common modules for all tracks in Business Programme.

It is well-known that Statistics is a science that deals with collection, description, analysis, interpretation, and presentation of data. Statistics can be used to describe a particular data set, termed descriptive statistics (BUS102) as well as to draw conclusions about the population from a particular data set, termed inferential statistics (BUS102 and BUS202). The course applies statistical methods in a business context in order to address business related questions and help make evidence based decisions. The course will provide students with the knowledge they need to become stronger analysts and better decision makers.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_50">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_50" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Introduction to Statistics</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>BUS102</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Introduction to Statistics</td>
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
											<td>The course helps students understand the relationship between statistics and the world, bringing life to the theory and methods. It incorporates an unprecedented amount of real and interesting data that will help students to connect statistics to their daily lives.

BUS102 is considered an introductory course for BUS202 (data analysis). At the undergraduate level, both modules (BUS102 and BUS202) are considered as part of common modules for all tracks in Business Programme.

It is well-known that Statistics is a science that deals with collection, description, analysis, interpretation, and presentation of data. Statistics can be used to describe a particular data set, termed descriptive statistics (BUS102) as well as to draw conclusions about the population from a particular data set, termed inferential statistics (BUS102 and BUS202). The course applies statistical methods in a business context in order to address business related questions and help make evidence based decisions. The course will provide students with the knowledge they need to become stronger analysts and better decision makers.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p style="text-align:justify;">&ZeroWidthSpace;&ZeroWidthSpace;The course covers basic statistical concepts and introduces some advanced topics and tools that are very useful for decision-makers in different business disciplines. The topics include descriptive statistics, probability distributions, sampling, and estimations for small and large samples of data (statistical inference). An emphasis will be given to the understanding, applicability of statistical analysis and interpretation of output using MS Excel spreadsheets and/ or any available open source analytical tools.<br><strong>&nbsp;</strong></p><p style="text-align:justify;"><strong>Attitudinal aims</strong></p><p style="text-align:justify;">In addition to specific learning outcomes, the course aims to shape the attitudes of learners regarding the field of Statistics. Specifically, the course aims to </p><p style="text-align:justify;">&nbsp;</p><p style="text-align:justify;">1. Motivate in students an intrinsic interest in statistical thinking. </p><p style="text-align:justify;">2. Instil the belief that Statistics is important for scientific research. </p><p style="text-align:justify;">3. Provide a foundation and motivation for exposure to statistical ideas subsequent to the course&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="line-height:115%;"><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;"><strong>A.
Knowledge and understanding</strong></span></p><p style="line-height:115%;"><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;"><strong>A1:</strong>
knowledge of how to formulate data analysis problems in a statistical
framework.</span></p><p style="line-height:115%;"><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;"><strong>A2:</strong>
knowledge of how to assemble relevant information and construct appropriate
arguments.</span></p><p style="line-height:115%;"><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;"><b>A3:</b>
knowledge of how to exercise judgment in selection and application of a wide
range of statistical tools and techniques.</span></p><p style="text-align:justify;"><strong>B. Cognitive skills</strong></p><p style="text-align:justify;"><strong>B1: </strong>the ability to approach statistical problems and tasks in a flexible way.<br></p><p style="text-align:justify;"><strong>B2:</strong> the ability to choose appropriate models for situations involving uncertainty, and understand their key elements and properties.<br></p><p style="text-align:justify;"><strong>B3: </strong>the ability to comment critically on choices of model and analyses resulting from them.&ZeroWidthSpace;<br></p><p style="text-align:justify;"><strong>B4: </strong>the ability to evaluate statistical evidence and to interpret the results of a statistical analysis</p><p style="text-align:justify;"><strong>B5: </strong>the ability to create statistical models and draw justifiable inferences<span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;"><br></span></p><span>&nbsp;</span><p><span lang="EN-GB"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB"><strong>C1: </strong>practically deal with numbers and
manipulate them confidently.</span></p><p><span lang="EN-GB"><strong>C2</strong><strong>:</strong> easily use a calculator and its
functions.</span></p>

<span class="ms-rteThemeFontFace-1" lang="EN-GB" style="font-size:13px;"><strong>C3:</strong> master the techniques of discounts,
mark-ups/markdowns, payroll, credit consumer, simple &amp; compounded
interests, and annuities</span><span class="ms-rteThemeFontFace-1">

</span><p><br>&nbsp;</p><p><strong>D. Key transferable skills&nbsp;</strong></p><p style="text-align:justify;"><strong>D1:</strong> Work with others effectively, participate as a member of a team and thus contribute to group effort.</p><p style="text-align:justify;"><strong>D2:</strong> Work hard to satisfy others expectations.</p><p style="text-align:justify;"><strong>D3:</strong> Exercise Leadership and communicate ideas clearly to convince others and responsibly challenge his classmates having other ideas, opinions, or methods of solving. </p><p style="text-align:justify;"><strong>D4:</strong> Collaborate with classmates to solve a problem and teach others new skills.</p><p style="text-align:justify;"><strong>D5:</strong> Apply technologies to task (exercises, problems, situations) and work with a variety of technologies and solve problems using calculators, and computers.<br></p></td>
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
                    BUS109&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Business Law – Country Specific <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Rules of law govern many aspects of business. An understanding of legal rules and ethical constraints provides a framework for making sound business decisions, facilitates commercial transactions, and promotes order in the marketplace.  

This module introduces the students to the fundamental concepts of commercial laws. It entails the survey of the country-specific judicial system, business ethics, contract laws, antitrust law and commercial agencies; contracts; property sales and secured transactions; insurance; commercial papers; agency; bailment; bankruptcy; banking operations, all in a comparative approach.
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
								<span class="modal-title">Business Law – Country Specific</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>BUS109</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Business Law – Country Specific</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>EL 111: Freshman English</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Rules of law govern many aspects of business. An understanding of legal rules and ethical constraints provides a framework for making sound business decisions, facilitates commercial transactions, and promotes order in the marketplace.  

This module introduces the students to the fundamental concepts of commercial laws. It entails the survey of the country-specific judicial system, business ethics, contract laws, antitrust law and commercial agencies; contracts; property sales and secured transactions; insurance; commercial papers; agency; bailment; bankruptcy; banking operations, all in a comparative approach.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p style="text-align:justify;">&ZeroWidthSpace;&ZeroWidthSpace;The main objective of the module is to help business students understand the legal aspect of common business activities and the formation and functioning of commercial companies along with the related ethical principles.&nbsp; </p><p style="text-align:justify;">&nbsp;</p><p style="text-align:justify;">This engaging module teaches students about the workings of business law by examining real case studies and examples. The material explores core issues in both national and international business law in depth while remaining brief and concise. </p><p style="text-align:justify;">&nbsp;<br></p><p style="text-align:justify;">Topics covered include: The basic elements of contract laws, negligence and product liability, property laws such as mortgages, landlord and tenant and personal property, Intellectual Property, Labour law, Environmental Law.&nbsp; </p><p style="text-align:justify;"><br>&nbsp;</p><p style="text-align:justify;">After studying the module students should be able to: <br></p><ol><li>Recognize legal and ethical issues when making business decisions. </li><li>Gain an enhanced understanding of legal rules and ethical constraints. </li><li>Improve analytical problem solving and ethical decision-making skills.&nbsp; </li><li>Apply knowledge and skills to address and manage potential problems before they become actual, expensive problems.&nbsp; </li><li>Evaluate expert advice and determine the extent to which it should be incorporated into business decisions. </li><li>Total understanding of the The Law of Contracts and Sales. </li></ol><p>Understanding and respect of the intellectual property rights and environmental laws.<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>A. Knowledge
and understanding</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1:<span>&nbsp; </span>The Legal Environment
of Business. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2:<span>&nbsp; </span>Constitutional
Principles. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3:<span>&nbsp; </span>Ethics, Social
Responsibility, and the Business Manager. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4: The
International Legal Environment of Business. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span><strong>B. Cognitive skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: Recognize, compare and contrast different ways of analyzing
business case studies and other material about contemporary business law
practice. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: Apply their knowledge in the analysis of practical business
law problems and issues. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3: Recognize, compare and contrast different interpretations of
and approaches to practical business law problems and issues.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: Analyze work-related cases and situations to identify problems
with an exploration of ethics that takes business law education a step further
by teaching students how to practice justly<span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Identify and communicate potential solutions based on
knowledge of theory and applying it to their own work situation as Business Law
uses tangible examples that students will be able to reference in their future
careers to introduce students to this important topic.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Read and précis written text materials for key salient points.
</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2: Communicate effectively in writing, showing recognition of
audience and purpose. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D3: Select data, information and ideas from different sources and
present in an appropriate fashion to support an argument. </span></p>

<span class="ms-rteFontSize-2" lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D4: Identify some of the
key strengths and needs of their own learning and identify opportunities to
address these.</span>&nbsp;</td>
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
                    “Introduction to Business” is an introductory course, which surveys the role of business in society. At its simplest level, business is the exchange of goods and services for mutual benefit or profit. Students will be exposed to a wide variety of topics including the terms, trends, organizational structure and opportunities inherent in this exchange, the course introduces the student to the contemporary business world, the business of managing, people in organizations, the principles of marketing, managing information, and financial issues.
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
											<td>EL111</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>“Introduction to Business” is an introductory course, which surveys the role of business in society. At its simplest level, business is the exchange of goods and services for mutual benefit or profit. Students will be exposed to a wide variety of topics including the terms, trends, organizational structure and opportunities inherent in this exchange, the course introduces the student to the contemporary business world, the business of managing, people in organizations, the principles of marketing, managing information, and financial issues.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">&ZeroWidthSpace;The primary objective is to give the student an understanding of
basic business principles. Global business, entrepreneurship, management,
marketing, information technology, and financial management will be discussed.
Another purpose of this course is to build a foundation of knowledge on the
different theoretical approaches to management and decision making • develop
analytical skills to identify the links between the functional areas in
management, organisations, management practices and the business environment.</span><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;"></span><p style="line-height:115%;"><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">Learning Objectives: Upon completion of the course students will
have a firm understanding of the following business topics:</span><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;"></span></p>

<ul><li><div style="line-height:115%;"><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">The
relationship between business and society in a free market economy</span></div></li><li><div style="line-height:115%;"><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">Common forms of business ownership</span></div></li><li><div style="line-height:115%;"><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">Business ethics and social
responsibility</span></div></li><li><div style="line-height:115%;"><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">International business and the global
economy</span></div></li><li><div style="line-height:115%;"><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">Fundamentals of business management</span></div></li><li><div style="line-height:115%;"><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">Business organization and structure</span></div></li><li><div style="line-height:115%;"><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">Human resources, motivation and
productivity</span></div></li><li><div style="line-height:115%;"><span lang="EN-GB" style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">Marketing, accounting, finance,
operations management and other business specialties</span><br></div></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;<strong>A. Knowledge and understanding</strong></p><p><strong><span lang="EN-GB" style="font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">A1</span></strong><span lang="EN-GB" style="font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">: Identify
business functions </span></p><p><strong><span lang="EN-GB" style="font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">A2</span></strong><span lang="EN-GB" style="font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">: Recognize
different business models and forms</span></p><p><strong><span lang="EN-GB" style="font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">A3</span></strong><span lang="EN-GB" style="font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">: Acquire
knowledge of business ethics and social responsibility</span></p>

<strong><span lang="EN-GB" style="font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">A4</span></strong><span lang="EN-GB" style="font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">: Be aquatinted with the fundamentals of management. </span><p>&ZeroWidthSpace;<br><strong>B. Cognitive skills</strong></p><p><strong><span lang="EN-GB" style="color:black;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">B1</span></strong><span lang="EN-GB" style="color:black;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">: Differentiate between business structures
and business forms.&ZeroWidthSpace;</span></p><p><strong><span lang="EN-GB" style="color:black;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">B2</span></strong><span lang="EN-GB" style="color:black;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">: Examine different models and theories and
its effect in business life.</span></p><p><strong><span lang="EN-GB" style="color:black;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">B3</span></strong><span lang="EN-GB" style="color:black;font-family:&quot;arial&quot;,sans-serif;font-size:11pt;">: analysing and evaluating different
perspectives, identifying biases and hidden assumptions in different models and
forms of businesses.</span></p>

<p><strong class="ms-rteThemeFontFace-1" style="font-size:13px;">C. Practical and professional skills</strong></p><p><span class="ms-rteFontFace-13" style="font-size:11pt;"><strong>C1</strong>: Analyse different business-related situations and forms.&nbsp;<br></span></p><p><span class="ms-rteFontFace-13" style="font-size:11pt;"><strong>C2</strong>: Deduce problems and solutions and its pathways<br></span></p><p><strong class="ms-rteThemeFontFace-1" style="font-size:13px;">D Key transferable skills&nbsp;</strong></p><p><span class="ms-rteFontFace-13" style="font-size:11pt;"><strong>D1</strong>: Read financial and business related reports<br></span></p><p><span class="ms-rteFontFace-13" style="font-size:11pt;"><strong>D2</strong>: Communicate knowledge and understanding of business issues to different stakeholders.&ZeroWidthSpace;<br></span></p><p><strong class="ms-rteFontFace-13" style="font-size:11pt;">D3</strong><span class="ms-rteFontFace-13" style="font-size:11pt;">: Analyse situations in an academic manner.</span><br></p><p><br>&nbsp;</p></td>
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
                    BUS115&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Small Business Management <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    BUS115 is an introductory four credit undergraduate course. It assumes no deep knowledge of business. Indeed, it provides students with an overview of business in an-increasingly global society. This is not a course of theory; it is more an application or "how-to" course. It is designed to increase awareness of the opportunities and challenges in today's business environment. The success of any business depends upon several factors: marketing, management and leadership, human resources, financing, logistics, planning, and knowledge of the business environment. An overview of business topics will be discussed including the entrepreneur's success factors, developing business plans, forms of business ownership, management and leadership styles, marketing and market research, technology and e-commerce, understanding financial statements and testing the feasibility and viability of a new venture.
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
								<span class="modal-title">Small Business Management</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>BUS115</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Small Business Management</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>BUS110</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>BUS115 is an introductory four credit undergraduate course. It assumes no deep knowledge of business. Indeed, it provides students with an overview of business in an-increasingly global society. This is not a course of theory; it is more an application or "how-to" course. It is designed to increase awareness of the opportunities and challenges in today's business environment. The success of any business depends upon several factors: marketing, management and leadership, human resources, financing, logistics, planning, and knowledge of the business environment. An overview of business topics will be discussed including the entrepreneur's success factors, developing business plans, forms of business ownership, management and leadership styles, marketing and market research, technology and e-commerce, understanding financial statements and testing the feasibility and viability of a new venture.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p style="text-align:justify;">&ZeroWidthSpace;The course develops the student's understanding of entrepreneurship and the needed competencies of the entrepreneur.&nbsp; The following topics will be emphasized: entrepreneur's success factors, developing business plans, understanding financial statements, completing market assessment, marketing and market research, and how to obtain financing for the new business venture. After studying the course, you should be able to: </p><ul><li>To possess a well-grounded understanding of essential entrepreneurial business principals.&nbsp; </li><li>To develop an understanding of important business issues as they relate to new ventures. </li><li>To identify, appreciate, and assess the knowledge, attitudes, and skills of an entrepreneur.</li><li>To study and observe entrepreneurial settings and entrepreneurial role models through exposure to actual business settings and experiences. </li><li>To have an expanded awareness of the resources available for creating a business plan.&nbsp; </li></ul><p>To establish a level of confidence in creating a business plan as a tool to assess, create and communicate a business concept. &ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><b>&ZeroWidthSpace;A. Knowledge
and understanding</b></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1: Entrepreneurship and the role of the entrepreneur in the
economic development of nations<span>&nbsp; </span>A2:
Entrepreneurial competencies </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2:
Understanding and writing the business plan</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3:<span>&nbsp; </span>Understanding financial statements and
completing sales forecasts and projections <span>&nbsp;</span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: Reflection and critical engagement into the differences
between franchising versus building your own business concept<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: Critical thinking, analysis, and synthesis </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3: Valuation and comparison of small business management. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: Time management, skills appropriate to business, such as
creativity, persuasion and attractiveness. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Study skills, learning to learn and reflecting on students’
own development as learners. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3: The ability to analyse work-related cases and situations to
identify challenges for organisations in developing responses in relation to
their environments. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C4: The application of course ideas to students’ own interactions
with organisations and life experiences. <span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Decision making and problem solving making a viable approach
to students to engage with data analysis, interpretation and extrapolation. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2: Market assessment: consumers, competitors, etc….<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D3: Identify some of the key strengths and needs of their own
learning and identify opportunities to address these.</span><br></p></td>
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
                    BUS202&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Data Analysis <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The module helps students understand the relationship between statistics and the world, bringing life to the theory and methods. It incorporates an unprecedented amount of real and interesting data that will help students to connect statistics to their daily lives. BUS202 Data Analysis is an extension of the module BUS102 Introduction to Statistics. At the undergraduate level, both modules (BUS102 and BUS202) are common modules for FBS, as a part of the faculty requirements. 
 
It is well-known that Statistics is a science that deals with collection, description, analysis, interpretation, and presentation of data. Statistics can be used to describe a particular data set, termed descriptive statistics as well as to draw conclusions about the population from a particular data set, termed inferential statistics. This module applies statistical methods in a business context in order to address business related questions and help make evidence based decisions. The module would provide students with the knowledge they need to become stronger analysts and better decision makers.

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
								<span class="modal-title">Data Analysis</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>BUS202</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Data Analysis</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>BUS101 &amp; BUS102</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>The module helps students understand the relationship between statistics and the world, bringing life to the theory and methods. It incorporates an unprecedented amount of real and interesting data that will help students to connect statistics to their daily lives. BUS202 Data Analysis is an extension of the module BUS102 Introduction to Statistics. At the undergraduate level, both modules (BUS102 and BUS202) are common modules for FBS, as a part of the faculty requirements. 
 
It is well-known that Statistics is a science that deals with collection, description, analysis, interpretation, and presentation of data. Statistics can be used to describe a particular data set, termed descriptive statistics as well as to draw conclusions about the population from a particular data set, termed inferential statistics. This module applies statistical methods in a business context in order to address business related questions and help make evidence based decisions. The module would provide students with the knowledge they need to become stronger analysts and better decision makers.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p style="text-align:justify;">&ZeroWidthSpace;As mentioned before this module is an extension of BUS102. The module covers a higher level of statistical concepts and introduces advanced topics and tools that are very useful for decisionmakers in different business disciplines. The topics include hypothesis testing, regression analysis, analysis of categorical data and time series.&nbsp;&nbsp; </p><p style="text-align:justify;">An emphasis will be given to the understanding, applicability of statistical analysis and interpretation of output using MS Excel spreadsheets and/ or any available open source statistical software. <br></p><p style="text-align:justify;">Attitudinal aims In addition to specific learning outcomes, the module aims to shape the attitudes of learners regarding the field of Statistics. Specifically, the module aims to&nbsp; </p><ol><li>Motivate in students an intrinsic interest in statistical thinking.&nbsp; </li><li>Instil the belief that Statistics is important for scientific research.&nbsp; </li></ol><p>3. Provide a foundation and motivation for exposure to statistical ideas subsequent to the module.<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>&ZeroWidthSpace;A. Knowledge
and understanding</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1: Knowledge of how to formulate data analysis problems in a
statistical framework. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2: Knowledge of how to assemble relevant information and
construct appropriate arguments. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3: Knowledge
of how to exercise judgment in selection and application of a wide range of
statistical tools and techniques.</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: the ability to approach statistical problems and tasks in a
flexible way.<span>&nbsp;&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: the ability to choose appropriate models for situations
involving uncertainty, and understand their key elements and properties </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3: the ability to comment critically on choices of model and
analyses resulting from them. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B4: the ability to evaluate statistical evidence and to interpret
the results of a statistical analysis </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B5: the ability to create statistical models and draw justifiable
inferences</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: confidently use a variety of hypothesis testing techniques to
test for different types of parameters. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: easily find/use different types of models including simple
regression, multiple regression, time series generated models (Moving Average
“MA”, Auto-Regressive “AR”) </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: work with others effectively and to participate as a member of
a team and thus contribute to group effort. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2: collaborate with classmates to solve a problem and teach
others new skills. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D3: work hard to satisfy others expectations. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D4: exercise Leadership and communicate ideas clearly to convince
others and responsibly challenge his classmates having other ideas, opinions,
or methods of solving.<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D5: communicate in writing relevant information accurately and
effectively, using a form, structure and style that suits the purpose. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D6: apply technologies to task (exercises, problems, situations)
and use information technology with confidence to develop statistical insight,
acquire statistical knowledge, present data to model, and solve problems.</span></p></td>
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
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_53">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_53" class="modal fade" role="dialog">
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
											<td>B207B</td>
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
											<td><p>&ZeroWidthSpace;The aims of this course are to:<br></p><p style="text-align:left;">Provide students with concepts and tangible strategic skills that can readily be put into practice in often&nbsp;&nbsp; changing business environments.&nbsp;<br>-Present the 21st century competitive/business landscape from a strategic management perspective and to assess how global and technological influences shape it</p><p style="text-align:left;">-Provide students with a critical overview of the main tools of contemporary strategic practice in organizations in a way which is relevant to their professional needs</p><p>Achieving the intended learning outcomes (covering both knowledge and skills) fully supports this aim.&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">&ZeroWidthSpace;<strong>A</strong><strong>.</strong><strong> </strong><strong>K</strong><strong>n</strong><strong>o</strong><strong>w</strong><strong>l</strong><strong>e</strong><strong>d</strong><strong>ge a</strong><strong>n</strong><strong>d</strong><strong> </strong><strong>u</strong><strong>n</strong><strong>d</strong><strong>erstan</strong><strong>d</strong><strong>i</strong><strong>ng</strong></span></p><p style="text-align:justify;line-height:115%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB" style="line-height:115%;">A1</span></strong><span lang="EN-GB" style="line-height:115%;">. The structure and dynamics of business environments; how
businesses seek to track and analyse their environments;</span></span></p><p style="text-align:justify;line-height:115%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB" style="line-height:115%;">A2</span></strong><span lang="EN-GB" style="line-height:115%;">. Markets, market economies and how they function; how consumers,
firms and governments behave as economic agents; why and how markets fail and
how this failure is managed;</span></span></p><p style="text-align:justify;line-height:115%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB" style="line-height:115%;">A3</span></strong><span lang="EN-GB" style="line-height:115%;">. Business processes and how they operate; the nature, structure
and functioning of organisations; how and why organisations are changing;&ZeroWidthSpace;</span></span></p><p style="text-align:justify;line-height:115%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB" style="line-height:115%;">A4</span></strong><span lang="EN-GB" style="line-height:115%;">. Key business functions such as Marketing, Human Resources,
Information Management, Accounting &amp; Finance, Operations – their nature and
contribution to organisational success, their historic origins and their
interactions;</span></span></p><p style="text-align:justify;line-height:115%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB" style="line-height:115%;">A5</span></strong><span lang="EN-GB" style="line-height:115%;">. How businesses develop strategies; the different forms and
theories of strategy;</span></span></p><p style="text-align:justify;line-height:115%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB" style="line-height:115%;">A6</span></strong><span lang="EN-GB" style="line-height:115%;">. How organisations make decisions and organise decision-making
processes; the various sources of decision-making irrationality; the nature,
role and implications of governmental, regional and supranational business
policy on businesses;</span></span></p><span class="ms-rteThemeFontFace-1" style="font-size:13px;">

</span><strong class="ms-rteThemeFontFace-1" style="font-size:13px;"><span lang="EN-GB">A7</span></strong><span class="ms-rteThemeFontFace-1" lang="EN-GB" style="font-size:13px;">. How to apply key ideas in mathematics, including some&nbsp;&nbsp; statistics, and algebra.</span><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><br><strong>B</strong><strong>.</strong><strong> </strong><strong>C</strong><strong>o</strong><strong>g</strong><strong>n</strong><strong>i</strong><strong>ti</strong><strong>v</strong><strong>e</strong><strong> </strong><strong>s</strong><strong>ki</strong><strong>ll</strong><strong>s</strong></span></p><p style="line-height:115%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB" style="line-height:115%;">B1</span></strong><span lang="EN-GB" style="line-height:115%;">.
Read material questioningly, identifying and recording key ideas and concepts
in business studies;</span></span></p><p style="line-height:115%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB" style="line-height:115%;">B2</span></strong><span lang="EN-GB" style="line-height:115%;">.
Synthesise material from a variety of sources, analysing and evaluating
different perspectives, identifying biases and hidden assumptions;</span></span></p><p style="line-height:115%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB" style="line-height:115%;">B3</span></strong><span lang="EN-GB" style="line-height:115%;">.
Classify, recognise and organise material in distinct and relevant categories;</span></span></p><div><span class="ms-rteThemeFontFace-1" style="font-size:13px;">

<strong><span lang="EN-GB">B4</span></strong><span lang="EN-GB">. Construct, defend and evaluate an argument, using relevant evidence,
giving reasons for conclusions.</span></span></div><div><span class="ms-rteThemeFontFace-1" lang="EN-GB" style="font-size:13px;"><br></span>&nbsp;</div><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>C</strong><strong>.</strong><strong> </strong><strong>P</strong><strong>ra</strong><strong>c</strong><strong>ti</strong><strong>c</strong><strong>a</strong><strong>l</strong><strong> </strong><strong>a</strong><strong>n</strong><strong>d pr</strong><strong>o</strong><strong>f</strong><strong>e</strong><strong>s</strong><strong>sion</strong><strong>a</strong><strong>l s</strong><strong>ki</strong><strong>ll</strong><strong>s</strong><br></span></p><p style="line-height:115%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB" style="line-height:115%;">C1</span></strong><span lang="EN-GB" style="line-height:115%;">. Transfer
and use relevant key skills in the workplace context;</span></span></p><p style="line-height:115%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB" style="line-height:115%;">C2</span></strong><span lang="EN-GB" style="line-height:115%;">.
Use the more specific knowledge, analytic skills and methods, rooted in the
different disciplines as a strong basis for work in many professions;</span></span></p><p style="line-height:115%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteThemeFontFace-1" lang="EN-GB" style="line-height:115%;font-size:13px;">Students will have become better informed, more
active and questioning members of an organisation by:</span></p><p style="line-height:115%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong><span lang="EN-GB" style="line-height:115%;">C3</span></strong><span lang="EN-GB" style="line-height:115%;">.
The ability to engage critically with the underlying challenges and problems
facing a business; </span></span></p><div><span class="ms-rteThemeFontFace-1" style="font-size:13px;">

<strong><span lang="EN-GB">C4</span></strong><span lang="EN-GB">. The ability to identify and evaluate conflicting arguments, including <span lang="EN-GB">recognising
the significance of different value positions in these arguments.</span></span></span></div><div><span class="ms-rteThemeFontFace-1" lang="EN-GB" style="font-size:13px;"><span lang="EN-GB"><br></span></span>&nbsp;</div><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>D </strong><strong>K</strong><strong>e</strong><strong>y</strong><strong> </strong><strong>t</strong><strong>ran</strong><strong>s</strong><strong>f</strong><strong>era</strong><strong>b</strong><strong>l</strong><strong>e s</strong><strong>k</strong><strong>i</strong><strong>l</strong><strong>l</strong><strong>s</strong></span></p><p style="text-align:justify;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>D1</strong>. Interpersonal skills of effective listening, negotiating, persuasion and presentation;<br></span></p><p style="text-align:justify;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>D2</strong>. Ability to conduct research into business and management issues, either individually or as part of a team for projects/dissertations/presentations. This requires familiarity with and an evaluative approach to a range of business data, sources of information and appropriate methodologies, and for such to inform the overall learning process; including the development of personal and team attributes and capabilities for entrepreneurial success;<br></span></p><p style="text-align:justify;"><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>D3</strong>. Self reflection and criticality including self awareness, openness and sensitivity to diversity in terms of people, cultures, business and management issues;&ZeroWidthSpace;<br></span></p><p><span style="font-size:13px;"><strong class="ms-rteThemeFontFace-1" style="font-size:13px;">D4</strong><span class="ms-rteThemeFontFace-1" style="font-size:13px;">. Skills of learning to learn and developing a continuing appetite for learning; reflective, adaptive and collaborative learning.</span></span><br></p></td>
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
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_94">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_94" class="modal fade" role="dialog">
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
											<td>The course introduces the student to the basics of Chinese (Mandarin). These include the alphabet, common everyday expressions, simple sentences, short dialogues and small paragraphs. The four skills of reading, writing, listening and speaking will be equally emphasized. However, as we live in the age of the image, students will have ample exposure to a variety of audio-visual material which boost their command of the language at the beginner’s level.  The communicative approach is to be adopted in face-to-face tutorials and the various methods of enabling students to learn on their own will be prioritized.</td>
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
                    CH102&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Chinese for Beginners (II) <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The course builds on what the student has learnt in level (1). Toward this end, it introduces the student to more everyday expressions, more widely-used short sentences, some compound and complex sentences, medium-size dialogues, and short passages. While the skills of listening and speaking will be receiving adequate attention, more emphasis is to be placed on the skills of reading and writing.  Face-to-face tutorials will be communicative and students will be empowered to learn on their own.
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
											<td>The course builds on what the student has learnt in level (1). Toward this end, it introduces the student to more everyday expressions, more widely-used short sentences, some compound and complex sentences, medium-size dialogues, and short passages. While the skills of listening and speaking will be receiving adequate attention, more emphasis is to be placed on the skills of reading and writing.  Face-to-face tutorials will be communicative and students will be empowered to learn on their own.</td>
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
                    DD209A&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Economics for Business <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This key introductory Level 5 course is the second in our degree in business studies and forms the core of the certificate in business studies- economic track. This module teaches Macroeconomics (DD209A) – the focus of most public debate – the student is engaged in policy debates and the problems of managing the national and global economy after a major economic crisis. Through this module, students will be enabled to place themselves as an economic analyst tackling problems in the national macro economy. The student will emerge with a good grasp of some fundamentals of economic theory including the application of basic game theory; an understanding of some key theoretical and policy debates in economics; and confidence in applying these theories and concepts to major economic policy challenges.  
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_24">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_24" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Economics for Business</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>DD209A</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Economics for Business</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>ECO101 and ECO102</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This key introductory Level 5 course is the second in our degree in business studies and forms the core of the certificate in business studies- economic track. This module teaches Macroeconomics (DD209A) – the focus of most public debate – the student is engaged in policy debates and the problems of managing the national and global economy after a major economic crisis. Through this module, students will be enabled to place themselves as an economic analyst tackling problems in the national macro economy. The student will emerge with a good grasp of some fundamentals of economic theory including the application of basic game theory; an understanding of some key theoretical and policy debates in economics; and confidence in applying these theories and concepts to major economic policy challenges.  </td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p style="text-align:justify;">&ZeroWidthSpace;&ZeroWidthSpace;The academic purpose of this course is designed to introduce learners to the internal and external elements of Macroeconomics. The module will have a student-cantered approach in developing and applying economic theories and debates to serious worldwide economic problems, and the critical assessment of proposed solutions. Transferable and vocational skills students will acquire include: <br></p><ol><li>The interpretation, manipulation and critique of economic evidence, including numerical data and basic statistical skills </li><li>Compare and contrast the most prominent economic traditions and theories of the last two centuries, widely used in public debate </li><li>Ability to build and support an argument in a discussion </li><li>Use and present modelling and simulation as methods of analysis of economic problems; simulate the macro economy under different policy scenarios&nbsp; </li></ol><p>5. Ability to engage in debates with other students, substantiating views with economic theory and evidence (coming from data, simulator or case studies)&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&ZeroWidthSpace;<strong>A. Knowledge
and understanding</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1.<span>&nbsp; </span>Modelling and its
importance in economic thinking; Be able to engage in the economic debate on
the role of demand stimulus vs. fiscal constraint in recovery; monetary policy;
and the scope for supply side restructuring and growth; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2. The use of abstraction in developing economic theories and
models; Recognise the implications of global imbalances in balance of payments
(deficits and surpluses), credit and debt, rising inequality, and the need for
‘rebalancing’ economies. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3. How specific economic models are constructed;<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4. Competing
theoretical perspectives and the assumptions underlying economic theories;
Understand how macroeconomics feeds into economic arguments for policy in areas
such as privatisation/nationalisation; trade restriction and promotion; welfare
state policies including health and education. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A5. How to
apply appropriate theories, models and concepts to economic problems, events
and processes.</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1. Construct and combine economic arguments and recognise the
differences between economic and other forms of argument;<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2. Manipulate economic models to analyse the impact of changes in
variables; Interpret, manipulate and criticise different types of data. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3. Evaluate economic theories and use them to explain and analyse
policy questions; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B4. Integrate diagrammatic and verbal analysis of economic issues;
</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B5. Interpret economic data presented in a variety of forms
including </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">basic regression results and undertake data analysis using
economic data and appropriate analytical tools; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B6. Search library catalogues and bibliographic databases and
select a range of academic literature focusing on a particular theoretical
proposition or economic issue and conduct fieldwork research.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><b>C. Practical and professional skills</b></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1. Demonstrate an awareness of skills and abilities in relation
to the requirements of own work role;<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2. Identify and evaluate the range of resources related to
working effectively; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3. Choosing appropriate methods and apply a model of a national economy
as constructed and used to analyse the roles of consumer spending, investment,
government taxes and spending and imports and exports;<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C4. Analyse the macroeconomic problems rather than a matter for
national governments; gain familiarity with a computer-based statistical
package and search and manipulate and present different sources of data. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C5. Seek for convenient policy to stabilise the economy and keep
unemployment and inflation low;<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C6. Communication of complex information, arguments and ideas in
ways appropriate to a business context and audience; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1. Read and synthesise information from a variety of sources for
a specified purpose and apply economic theory to real-life situations. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2. Read and construct scale drawings, graphs, charts and diagrams
from numerical data; read and interpret large and complex numerical data sets; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D3. Carry out multistage calculations with numbers of any size
incorporating the use of powers and roots; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D4. Calculate measures of average distribution; apply standard
formulae, equations and expressions in calculating economic measures and
indicators; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D5. Select and use appropriate methods to illustrate findings,
show trends and make comparisons; numerical and verbal analysis of economic
issues. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p>

<span class="ms-rteFontSize-2" lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D6.&nbsp; Work with qualitative and quantitative data,
drawing appropriate conclusions based on findings, including how possible
sources of error may affect the results.</span><p><br>&nbsp;</p></td>
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
                    DD209B&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Economics for Business-Microeconomics <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This key introductory Level 5 course is the second in our degree in business studies and forms the core of the certificate in business studies- economic track. This module teaches Microeconomics (DD209B) – the focus of most public debate – the student is engaged in policy debates and the problems of managing the national and global economy after a major economic crisis. The D209B module addresses the recurrent themes of inequalities and imbalances. It takes a global perspective on the challenges faced by national economies and the debates on the roles for government. It focuses particular on the interacting roles of trade policy and government welfare policies in addressing and mitigating inequality within and between countries.   
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
								<span class="modal-title">Economics for Business-Microeconomics</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>DD209B</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Economics for Business-Microeconomics</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>DD209A</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This key introductory Level 5 course is the second in our degree in business studies and forms the core of the certificate in business studies- economic track. This module teaches Microeconomics (DD209B) – the focus of most public debate – the student is engaged in policy debates and the problems of managing the national and global economy after a major economic crisis. The D209B module addresses the recurrent themes of inequalities and imbalances. It takes a global perspective on the challenges faced by national economies and the debates on the roles for government. It focuses particular on the interacting roles of trade policy and government welfare policies in addressing and mitigating inequality within and between countries.   </td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;The academic purpose of this course is designed to introduce learners to the most important elements of Microeconomics. The module will have a student-centered approach in developing and applying economic theories and debates to serious worldwide economic problems, and the critical assessment of proposed solutions. Transferable and vocational skills students will acquire include:&nbsp; </p><ol><li>Exploring the decision-making processes within firms that drive the growth of an economy.&nbsp; </li><li>Compare and contrast the most prominent economic traditions and theories of the last two centuries, widely used in public debate </li><li>Developing an understanding of the theory of the firm and the working of markets. Ability to build and support an argument in a discussion </li></ol><p>Analysing how global trade and the pursuit of growth creates imbalances that may have caused a macroeconomic crisis. &ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><b>A. Knowledge
and understanding</b></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1. Modelling and its importance in economic thinking; Be able to
engage in the economic debate on the role of demand stimulus vs. fiscal
constraint in recovery; and the scope for supply side restructuring and growth;
</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2. The use of abstraction in developing economic theories and
models; Recognise the implications of global imbalances in balance of payments
(deficits and surpluses), credit and debt, rising inequality, and the need for
‘rebalancing’ economies. A3. How specific economic models are constructed;<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4. Competing theoretical perspectives and the assumptions
underlying economic theories; Understand how microeconomics feeds into economic
arguments for policy in areas such as trade restriction and promotion; welfare
state policies including health and education. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A5. How to
apply appropriate theories, models and concepts to economic problems, events
and processes. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1. Construct and combine economic arguments and recognise the
differences between economic and other forms of argument;<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2. Manipulate economic models to analyse the impact of changes in
variables; Interpret, manipulate and criticise different types of data. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3. Evaluate economic theories and use them to explain and analyse
policy questions; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B4. Integrate diagrammatic and verbal analysis of economic issues;
</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B5. Interpret economic data presented in a variety of forms
including basic regression results and undertake data analysis using economic
data and appropriate analytical tools; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B6. Search library catalogues and bibliographic databases and
select a range of academic literature focusing on a particular theoretical
proposition or economic issue and conduct fieldwork research.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1. Demonstrate an awareness of skills and abilities in relation
to the requirements of own work role;<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2. Identify and evaluate the range of resources related to
working effectively; <span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3. Choosing appropriate methods and apply a model of a national
economy as constructed and used to analyse the roles of consumer spending,
investment, government taxes and spending and imports and exports;<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C4. Analyse the microeconomic problems, gain familiarity with a
computer-based statistical package and search and manipulate and present
different sources of data. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C5. Communication of complex information, arguments and ideas in
ways appropriate to a business context and audience; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C6. Problem-solving and decision-making using appropriate
quantitative and qualitative skills including data analysis, interpretation and
extrapolation </span></p>

<p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1. Read and synthesise information from a variety of sources for
a specified purpose and apply economic theory to real-life situations. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2. Read and construct scale drawings, graphs, charts and diagrams
from numerical data; read and interpret large and complex numerical data sets; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D3. Carry out multistage calculations with numbers of any size
incorporating the use of powers and roots; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D4. Calculate measures of average distribution; apply standard
formulae, equations and expressions in calculating economic measures and
indicators; &ZeroWidthSpace;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><br></span>&nbsp;</p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D5. Select and use appropriate methods to illustrate findings,
show trends and make comparisons; numerical and verbal analysis of economic
issues. &ZeroWidthSpace;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><br></span>&nbsp;</p>

<span class="ms-rteFontSize-2" lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D6.&nbsp; Work with qualitative and quantitative data,
drawing appropriate conclusions based on findings, including how possible
sources of error may affect the results.</span>&nbsp;</td>
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
                    DD309A&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Doing Economics <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Doing economics: people, markets and policy is a sixty-point third level course which teaches
economic theories that explain the behaviour of people in households, firms, markets and
governments. This course is split into two parts, D309A and D309B with 30 points each. It presents alternative economic explanations that will enable students to make their own critical
judgments of which theory serves which purpose best. The course also equips students with the
research skills that they’ll need to conduct their own project on a topic they want to know more
about. At the end of the course, students should have developed a more critical view of the socioeconomic world in which they live. The course will equip them with the theoretical tools
necessary to investigate recent developments in the global economy. A pluralist view of
economic theory is adopted, enabling students to appreciate the debates between different
approaches. The first part of the course teaches intermediate microeconomics with an emphasis
on both economic theory and its applications. The second part of the course is project-based;
students will be able to specialize in an area of their choice and carry out their own research
project.

D309a (first part of the course) is divided into three blocks 1, 2 and 3 plus two weeks of work
that introduce methods used by economists to test the relevance of their models using data. Block 1, People and Households; Block 2, Firms and Industries; and Block 3, Markets and Governments

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_22">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_22" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Doing Economics</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>DD309A</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Doing Economics</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>DD209B</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Doing economics: people, markets and policy is a sixty-point third level course which teaches
economic theories that explain the behaviour of people in households, firms, markets and
governments. This course is split into two parts, D309A and D309B with 30 points each. It presents alternative economic explanations that will enable students to make their own critical
judgments of which theory serves which purpose best. The course also equips students with the
research skills that they’ll need to conduct their own project on a topic they want to know more
about. At the end of the course, students should have developed a more critical view of the socioeconomic world in which they live. The course will equip them with the theoretical tools
necessary to investigate recent developments in the global economy. A pluralist view of
economic theory is adopted, enabling students to appreciate the debates between different
approaches. The first part of the course teaches intermediate microeconomics with an emphasis
on both economic theory and its applications. The second part of the course is project-based;
students will be able to specialize in an area of their choice and carry out their own research
project.

D309a (first part of the course) is divided into three blocks 1, 2 and 3 plus two weeks of work
that introduce methods used by economists to test the relevance of their models using data. Block 1, People and Households; Block 2, Firms and Industries; and Block 3, Markets and Governments
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;The aim of the course is to
provide students with a critical overview of the main tools of doing<font face="&quot;Segoe UI&quot;,&quot;Segoe&quot;,Tahoma,Helvetica,Arial,sans-serif"> </font></span><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">economies focusing on people,
markets and policy. It thus places emphasis on the theoretical<font face="&quot;Segoe UI&quot;,&quot;Segoe&quot;,Tahoma,Helvetica,Arial,sans-serif"> </font></span><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">underpinnings of the economic
theories, and the debates which surround it, as well as </span><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">developing practical skills
relevant to work in a range of organisations. Achieving the intended<font face="&quot;Segoe UI&quot;,&quot;Segoe&quot;,Tahoma,Helvetica,Arial,sans-serif"> </font></span><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">learning outcomes (covering both
knowledge and skills) fully supports this aim. This is a Level<font face="&quot;Segoe UI&quot;,&quot;Segoe&quot;,Tahoma,Helvetica,Arial,sans-serif"> </font></span><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">3 course. Level 3 courses build on
study skills and subject knowledge acquired from studies at </span><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">Levels 1 and 2. The students
should take Economics and economic change (DD202) course </span><em><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">before</span></em><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"> studying
DD309.&ZeroWidthSpace;</span>

<br></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><b>A. Knowledge and understanding</b></p><p>A1 : How decisions taken in various contexts, such as consumption, labour market participation, savings, investment in education and training. And how households, as well as individuals, can make decisions.</p><p>A2: Key theories underpinning the efficiency and productivity in the production of goods and services. Although the issues about choice of technology, entrepreneurship, innovation, employment relations, outsourcing and competition policy</p><p>A3: The overall organisation of the economy. The strengths and weaknesses of markets and governments in the organisation of economic activities, explores issues concerning the environment and ethics, and looks at economic theory that underpins government behaviour.</p><p>A4: Economic theories and their applications to various areas. Three available theoretical strands: environmental economics, business and finance or economics and society.</p><p>A5; Research Methods, how to carry out a literature review and then choose which research methods to be applied in A6. The qualitative methods – which include interviewing and case studies – and quantitative methods, which involve analysis of economic data.</p><p style="text-align:justify;">A6: Project work, choosing and completing a project. </p><p style="text-align:justify;">&nbsp;</p><p style="text-align:justify;"><strong>B. Cognitive skills</strong></p><p>B1: Thinking strategically in the context of a case study</p><p>B2: Critical thinking, analysis and synthesis: including identifying and questioning assumptions, weighing evidence appropriately, identifying and challenging false logic or reasoning, and generalising in a way which recognises the limits of knowledge in firm.</p><p>B3: Evaluation and comparison of competing perspectives from a variety of sources, including some informed by current issues or research developments.</p><p style="text-align:justify;">B4: The ability to argue relevantly and to justify a point of view </p><p style="text-align:justify;">&nbsp;</p><p style="text-align:justify;"><strong>C. Practical and professional skills</strong></p><p>C1 : Communication of complex information, arguments and ideas in ways appropriate to a business context and audience.</p><p>C2: Problem-solving and decision-making using appropriate quantitative and qualitative skills including data analysis, interpretation and extrapolation.</p><p>C3: Effective performance in a team environment in a virtual context.</p><p>C4. The application of course ideas to students' own interactions with organisations and life experiences.</p><p>C5: Selecting and using information and communication technologies for business purposes.</p><p>&nbsp;</p><p style="text-align:justify;"><strong>D Key transferable skills</strong></p><p>D1 : Engagement, as appropriate, with practical and professional business strategy skills and ethical issues.&ZeroWidthSpace;<br></p></td>
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
                    DD309B&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Doing economics: people, markets and policy <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Doing economics: people, markets and policy (Part B) is a thirty point third level course which teaches economic theories that explain the behaviour of people in households, firms, markets and governments. The course equips students with the research skills that they’ll need to conduct their own project on a topic they want to know more about. At the end of the course, students should have developed a more critical view of the socio-economic world in which they live. DD309b (second part of the course is divided into Blocks 4, 5 and 6.
Block 4, Optional strands, teaches further economic theory and its applications to various areas. Students should choose one of three available theoretical strands: environmental economics, business and finance or economics and society. In Block 5, Research Methods, students will learn how to carry out a literature review and then choose which research methods they plan to use for their project. They can choose between qualitative methods – which include interviewing and case studies – and quantitative methods, which involve analysis of economic data. In Block 6, Project Work, students will work towards their end-of-module assessment, completing a project of their choice.
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
								<span class="modal-title">Doing economics: people, markets and policy</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>DD309B</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Doing economics: people, markets and policy</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>DD309A </td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Doing economics: people, markets and policy (Part B) is a thirty point third level course which teaches economic theories that explain the behaviour of people in households, firms, markets and governments. The course equips students with the research skills that they’ll need to conduct their own project on a topic they want to know more about. At the end of the course, students should have developed a more critical view of the socio-economic world in which they live. DD309b (second part of the course is divided into Blocks 4, 5 and 6.
Block 4, Optional strands, teaches further economic theory and its applications to various areas. Students should choose one of three available theoretical strands: environmental economics, business and finance or economics and society. In Block 5, Research Methods, students will learn how to carry out a literature review and then choose which research methods they plan to use for their project. They can choose between qualitative methods – which include interviewing and case studies – and quantitative methods, which involve analysis of economic data. In Block 6, Project Work, students will work towards their end-of-module assessment, completing a project of their choice.</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;The aim of the course is to provide students with a critical overview of the main tools of doing economies focusing on people, markets and policy. It thus places emphasis on the theoretical underpinnings of the economic theories, and the debates which surround it, as well as developing practical skills relevant to work in a range of organisations. Achieving the intended learning outcomes (covering both knowledge and skills) fully supports this aim. This is a Level 3 course. Level 3 courses build on study skills and subject knowledge acquired from studies at Levels 1 and 2. The students should take Economics and economic change (DD209) course before studying DD309.&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><b>A. Knowledge
and understanding</b></span><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1 :<span>&nbsp; </span>Modeling and its importance in economic
thinking; </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2 : The use
of abstraction in developing economic theories and models; </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3 : How
specific economic models are constructed; A4:<span>&nbsp;
</span>Competing theoretical perspectives and the assumptions underlying
economic theories; <span>&nbsp;</span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&ZeroWidthSpace;&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1 : Construct economic arguments and recognise the differences
between economic and other forms of argument; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: Manipulate economic models to analyse the impact of changes in
variables; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3 : Evaluate economic theories and use them to explain and
analyse social issues and policy questions; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B4 : Integrate diagrammatic and verbal analysis of economic
issues;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1:<span>&nbsp; </span>Transfer and use
relevant key skills in the workplace context; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Use the more specific knowledge, analytic skills and methods, rooted
in the different disciplines as a strong basis for work in many professions.
Students will have become better informed, more active and … questioning
members of an organisation.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3 :The ability to engage critically with the underlying
challenges and problems facing a business;<span>&nbsp;
</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C4: The ability to identify and evaluate conflicting arguments,
including recognising the significance of different value positions in these
arguments.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Read and synthesise information from a variety of sources for
a specified purpose. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2: Read and construct scale drawings, graphs, charts and diagrams
from numerical data; read and interpret large and complex numerical data sets; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D3 : Calculate measures of average and distribution; apply
standard formulae, equations and expressions in calculating economic measures
and indicators; </span></p>

<span class="ms-rteFontSize-2" lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D4: Select and use
appropriate methods to illustrate findings, show trends and make comparisons.</span>&nbsp;</td>
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
                    ECO101&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Principle of Microeconomics <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This key introductory Level 1 course is the first economics module in our degree in business studies and forms the core of business studies- economics track. Students should first understand the economic problem before they move to learn its economic implications and economic changes. Every day people make decisions, what to buy and what to sell? All people are participating in consumption or production. These activities are the basic units of an economy and are concerned with the economic problem: how best to satisfy unlimited wants using the limited available resources. This module develops skills such as logical and analytical thinking and problem-solving skills. It is designed to explain the theoretical ideas and applies them to real life examples and case studies from the Arab region, without ignoring the international aspects. Therefore, this module directly addresses the Arab countries’ characteristics, problems, and economic policies. For some of students, economics is not the main area of study. However, understanding of basic economic concepts will still prove useful to all students whatever direction their studies and subsequent career may take.  

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
								<span class="modal-title">Principle of Microeconomics</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>ECO101</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Principle of Microeconomics</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>BUS110</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This key introductory Level 1 course is the first economics module in our degree in business studies and forms the core of business studies- economics track. Students should first understand the economic problem before they move to learn its economic implications and economic changes. Every day people make decisions, what to buy and what to sell? All people are participating in consumption or production. These activities are the basic units of an economy and are concerned with the economic problem: how best to satisfy unlimited wants using the limited available resources. This module develops skills such as logical and analytical thinking and problem-solving skills. It is designed to explain the theoretical ideas and applies them to real life examples and case studies from the Arab region, without ignoring the international aspects. Therefore, this module directly addresses the Arab countries’ characteristics, problems, and economic policies. For some of students, economics is not the main area of study. However, understanding of basic economic concepts will still prove useful to all students whatever direction their studies and subsequent career may take.  
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;The academic purpose of this course is designed to introduce learners to the internal and external elements of Microeconomics. Students are not expected to have taken any courses in economics, or to have any knowledge or experience of ICT. Nevertheless, this is a Level 2 course and students need the general study techniques appropriate to Level 2 study in the social sciences. After studying the module students should be able to: <br></p><ul><li>understand the domain of economics as a social theory </li><li>understand the main analytical tools which are used in economic analysis </li><li>learn the main conclusions derived from economic analysis and to develop their understanding of the organisational and policy implications </li></ul><p>to participate in debates on economic matters.&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&ZeroWidthSpace;<b>A. Knowledge
and understanding</b></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1: A strong
set of introductory chapters.<span>&nbsp; </span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2: Early
coverage of policy issues.<span>&nbsp; </span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3: Complete
coverage of monopolistic competition. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: Recognise, compare, and contrast different ways of analysing
business case studies within the Arabian region and other material about
contemporary business practice. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: Apply their knowledge in the analysis of practical business
problems and issues. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3: Recognise, compare and contrast different interpretations of
and approaches to practical business problems and issues </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><b>C. Practical and professional skills</b></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: The ability to understand the labour market and other factors
of production. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Pricing strategy </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><br></span>&nbsp;</p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Students develop many transferable skills that are highly
valued by employers such as time management, self-reliance, problem-solving,
the ability to understand and evaluate new concepts, and prioritising effectively.
Skills required include:<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">i) effective communication skills – both written and oral (These
are extremely important, as is the ability to work well as part of a
team.)<span>&nbsp;&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">ii)taking the initiative in the classroom but also allowing the
students enough freedom to further develop their own personality and
abilities<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">iii) working closely with other teachers, parents and other
education professionals<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">iv) creativity in presenting ideas </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">v) time management both inside and outside the classroom </span></p>

<span class="ms-rteFontSize-2" lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">vi) enthusiasm, patience</span><br></td>
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
                    ECO102&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Principle of Macroeconomics <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This key introductory Level 1 course is the first economics module in our degree in business studies and forms the core of business studies- economics track. Students should first understand the economic problem before they move to learn its economic implications and economic changes. Every day people make decisions, what to buy and what to sell? All people are participating in consumption or production. These activities are the basic units of an economy and are concerned with the economic problem: how best to satisfy unlimited wants using the limited available resources. This module develops skills such as logical and analytical thinking and problem-solving skills. It is designed to explain the theoretical ideas and applies them to real life examples and case studies from the Arab region, without ignoring the international aspects. Therefore, this module directly addresses the Arab countries’ characteristics, problems, and economic policies. For some of students, economics is not the main area of study. However, understanding of basic economic concepts will still prove useful to all students whatever direction their studies and subsequent career may take.  

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_27">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_27" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Principle of Macroeconomics</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>ECO102</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Principle of Macroeconomics</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>BUS110</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>This key introductory Level 1 course is the first economics module in our degree in business studies and forms the core of business studies- economics track. Students should first understand the economic problem before they move to learn its economic implications and economic changes. Every day people make decisions, what to buy and what to sell? All people are participating in consumption or production. These activities are the basic units of an economy and are concerned with the economic problem: how best to satisfy unlimited wants using the limited available resources. This module develops skills such as logical and analytical thinking and problem-solving skills. It is designed to explain the theoretical ideas and applies them to real life examples and case studies from the Arab region, without ignoring the international aspects. Therefore, this module directly addresses the Arab countries’ characteristics, problems, and economic policies. For some of students, economics is not the main area of study. However, understanding of basic economic concepts will still prove useful to all students whatever direction their studies and subsequent career may take.  
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;The academic purpose of this course is designed to introduce learners to the internal and external elements of Microeconomics. Students are not expected to have taken any courses in economics, or to have any knowledge or experience of ICT. Nevertheless, this is a Level 2 course and students need the general study techniques appropriate to Level 2 study in the social sciences. After studying the module students should be able to: <br></p><ul><li>understand the domain of economics as a social theory </li><li>understand the main analytical tools which are used in economic analysis </li><li>learn the main conclusions derived from economic analysis and to develop their understanding of the organisational and policy implications to participate in debates on economic matters.&ZeroWidthSpace;<br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><b>&ZeroWidthSpace;A. Knowledge
and understanding</b></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1: A strong
set of introductory chapters.<span>&nbsp; </span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2: Early
coverage of policy issues.<span>&nbsp; </span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3: Complete
coverage of monopolistic competition. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: Recognise, compare, and contrast different ways of analysing
business case studies within the Arabian region and other material about
contemporary business practice. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: Apply their knowledge in the analysis of practical business
problems and issues. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3: Recognise, compare and contrast different interpretations of
and approaches to practical business problems and issues </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: The ability to understand the labour market and other factors
of production. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Pricing strategy </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><br></span>&nbsp;</p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Students develop many transferable skills that are highly
valued by employers such as time management, self-reliance, problem-solving,
the ability to understand and evaluate new concepts, and prioritising effectively.
Skills required include:<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">i) effective communication skills – both written and oral (These
are extremely important, as is the ability to work well as part of a
team.)<span>&nbsp;&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">ii)taking the initiative in the classroom but also allowing the
students enough freedom to further develop their own personality and
abilities<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">iii) working closely with other teachers, parents and other
education professionals<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">iv) creativity in presenting ideas </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">v) time management both inside and outside the classroom </span></p>

<span class="ms-rteFontSize-2" lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">vi) enthusiasm, patience</span><br></td>
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
                    ECO340&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Managerial Economics <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Business entities operate in economic turbulent environments. Under these constraints, decisions taken by managers of business units can vary and differ depending on the manager’s and the company’s pursuit of goals and objectives. Proper economic analysis and use of appropriate techniques and tools are therefore mandatory for managers and decision makers. This module highlights the role of economics in business decision-making and how economics is relevant in other areas of management such as marketing and operations management. The module can be used to understand economic aspects of business problems and business environment using theories, tools, techniques and relevant case studies and examples. Basic skills of quantitative proficiency is required in order to understand pricing decisions techniques, variation of supply and demand, risk analysis, investment and the growth of the firm. This module provides students with a solid base of managerial economics study and practice.  
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
								<span class="modal-title">Managerial Economics</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>ECO340</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Managerial Economics</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>DD209B</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Business entities operate in economic turbulent environments. Under these constraints, decisions taken by managers of business units can vary and differ depending on the manager’s and the company’s pursuit of goals and objectives. Proper economic analysis and use of appropriate techniques and tools are therefore mandatory for managers and decision makers. This module highlights the role of economics in business decision-making and how economics is relevant in other areas of management such as marketing and operations management. The module can be used to understand economic aspects of business problems and business environment using theories, tools, techniques and relevant case studies and examples. Basic skills of quantitative proficiency is required in order to understand pricing decisions techniques, variation of supply and demand, risk analysis, investment and the growth of the firm. This module provides students with a solid base of managerial economics study and practice.  </td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td>&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;&ZeroWidthSpace;ECO340's academic aim is to introduce students to number of managerial concepts and theories of economics in order to understand and explain the behavior decision and decision-making of business firms and aspects of the market economy.&nbsp; <p>&nbsp;</p><p>It also develops the students' knowledge of economics as well as skills in problem-solving, decision making, and written and oral communication. ECO340 also aims to prepares students for business-economics concepts and making sense of the business-world. Thus, after studying the course, the students should be able to:&nbsp; </p><ol><li>Understand and apply a toolbox of fundamental concepts and theories of economics to guide managerial decision-making by individuals and business units.</li><li>Explain the nature and role of models and theories in economic analysis.</li><li>Explain the concepts of supply/demand/market equilibrium and their determinants. </li><li>Identify the main characteristics of different market types (perfect competition, monopoly and oligopoly) and predict price and output outcomes. </li><li>Apply economic models to for production and cost estimation.&nbsp;</li><li>Identify and explain the challenges and opportunities for today's managers.&ZeroWidthSpace;&ZeroWidthSpace;<br></li></ol></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&ZeroWidthSpace;<b>A. Knowledge
and understanding</b></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1 : Understand the economic environment that affect business
strategies, business behaviour and managerial decisions in order to realize
firms’ goals and objectives. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2 : Identify the determinants and variation of supply and demand
and their impact in the context of local economy. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3: Understand the importance of production functions in
managerial decisions. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4:
Understand the importance of cost in managerial decisions. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: Identify economic factors determining the firms’ decisions. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: Evaluate and interpret economic ideas, views and evidence. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3: Analyse demand estimation and forecasting </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B4: Identify the relation between production and cost </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B5: Identify and explain issues related to pricing and output
decisions</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: apply the economic way of thinking in order to identify
microeconomic problems (market resources allocation, prices rise and fall,
budgets allocation, production decisions...) </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Implement managerial decisions in high-risks environment and
turbulent economies</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3: Apply key concepts and theories of economics to managerial
decision making </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C4: Implement appropriate pricing strategies and output decisions
in different market types </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C5: Use tools and techniques of economics to improve managerial
decision making </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Develop a broad and inclusive understanding of how the
economic environment affects business strategies and decision making in
domestic and global economy. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2: Develop effective communication, both in speaking and writing
to convey solid arguments while adapting the language approach to the relevant
business situation and audience. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D3: Identify some of the key strengths and needs of their own
learning and recognize opportunities to address these. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D4:<span>&nbsp; </span>Effectively use
information and communication technologies when analysing economic situations
and using appropriate tools for managers’ decision-making.&nbsp;</span><br></p></td>
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
                    ECO341&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Economic Development <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Economic development is the process of gradual improvement in the material well-being of individuals. At the macro level, development economics studies why some countries have high standards of living, while others do not. At the micro level, development studies the functioning of markets in low income countries, with the ultimate goal of addressing market failures and lifting individuals out of poverty. Almost all topics in economics have a counterpart in development economics. The context of developing countries proves to be challenging for conventional economic models due to the prevalence of market failures. The situation often requires a careful investigation of the plausibility of assumptions in a developing context. Based on that, the course will cover mainly, among other topics, analytical approaches to the economic problems of developing nations. Topics include deep-rooted and new directions in development economics thinking, the welfare economics of poverty and inequality, empirical evidence on who benefits from economic development, labour market models, and public policy evaluation. 
                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_54">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_54" class="modal fade" role="dialog">
					<div class="modal-dialog modal-lg modal-dialog-centered">
						<!-- Modal content-->
						<div class="modal-content">
							<div class="modal-header">
								<span class="modal-title">Economic Development</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>ECO341</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Economic Development</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>DD209B</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Economic development is the process of gradual improvement in the material well-being of individuals. At the macro level, development economics studies why some countries have high standards of living, while others do not. At the micro level, development studies the functioning of markets in low income countries, with the ultimate goal of addressing market failures and lifting individuals out of poverty. Almost all topics in economics have a counterpart in development economics. The context of developing countries proves to be challenging for conventional economic models due to the prevalence of market failures. The situation often requires a careful investigation of the plausibility of assumptions in a developing context. Based on that, the course will cover mainly, among other topics, analytical approaches to the economic problems of developing nations. Topics include deep-rooted and new directions in development economics thinking, the welfare economics of poverty and inequality, empirical evidence on who benefits from economic development, labour market models, and public policy evaluation. </td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p style="text-align:justify;line-height:115%;"><span style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:13px;">&ZeroWidthSpace;The aim of this course is to introduce students to </span></p><p style="text-align:justify;line-height:115%;"><span style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:13px;">1. the theoretical foundations of development economics and also to
recent advances in the use of empirical methods in the study of developing
countries. </span></p><p style="text-align:justify;line-height:115%;"><span style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:13px;">2. apply the tools of economic analysis to problems of growth,
poverty, and environmental sustainability in developing countries. </span></p><p style="text-align:justify;line-height:115%;"><span style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:13px;">3. analyze the economic, social, and environmental impacts of
specific initiatives and promote development through policies and investment
projects</span></p><p style="text-align:justify;line-height:115%;"><span style="line-height:115%;font-family:&quot;arial&quot;,sans-serif;font-size:13px;">4. use economic data to conduct development analyses such as growth
diagnostics, poverty assessments, impact analysis of development projects, and
environmental impact assessments</span></p><span style="font-size:13px;">

</span><span lang="EN-GB" style="font-family:&quot;arial&quot;,sans-serif;font-size:13px;">5. prepare the corresponding reports for
international development agencies and policy makers. </span>&ZeroWidthSpace;<br></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p><span class="ms-rteThemeFontFace-1" style="font-size:13px;"><strong>&ZeroWidthSpace;A. </strong><span lang="EN-GB"><strong>Knowledge
and Understanding&nbsp;</strong></span></span></p><p style="line-height:150%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteFontFace-13" lang="EN-GB" style="line-height:150%;font-size:13px;">A1. Gain knowledge and understanding of the
theories,&nbsp; </span></p><p style="line-height:150%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteFontFace-13" lang="EN-GB" style="line-height:150%;font-size:13px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
principles, historical trends, current issues and practices </span></p><p style="line-height:150%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteFontFace-13" lang="EN-GB" style="line-height:150%;font-size:13px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
relevant to economic development. </span></p><p style="line-height:150%;text-indent:-21.3pt;margin-left:21.3pt;"><span style="font-size:13px;"><span class="ms-rteFontFace-13" lang="EN-GB" style="line-height:150%;font-size:13px;">A2.&nbsp;
Understand measurement of economic growth, poverty </span><span class="ms-rteFontFace-13" lang="EN-GB" style="line-height:150%;font-size:13px;">and inequality, agriculture and industrialization, </span></span></p><p style="margin:0px 0px 10px 21.3pt;text-align:left;color:#444444;text-transform:none;line-height:150%;text-indent:-21.3pt;letter-spacing:normal;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13" lang="EN-GB" style="line-height:150%;font-size:13px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
population, education and human capital, health and </span></p><p style="margin:0px 0px 10px 21.3pt;text-align:left;color:#444444;text-transform:none;line-height:150%;text-indent:-21.3pt;letter-spacing:normal;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13" lang="EN-GB" style="line-height:150%;font-size:13px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
nutrition, savings and credits; and trade and </span></p><p style="margin:0px 0px 10px 21.3pt;text-align:left;color:#444444;text-transform:none;line-height:150%;text-indent:-21.3pt;letter-spacing:normal;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13" lang="EN-GB" style="line-height:150%;font-size:13px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
development. </span></p><p style="line-height:150%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteFontFace-13" lang="EN-GB" style="line-height:150%;font-size:13px;">A3. Understand what affects&nbsp; economic growth, inequality and <span style="text-align:left;color:#444444;text-transform:none;line-height:150%;text-indent:-28.4px;letter-spacing:normal;font-family:&quot;arial&quot;,sans-serif;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;display:inline !important;white-space:normal;orphans:2;float:none;">poverty</span><span style="text-align:left;color:#444444;text-transform:none;line-height:150%;text-indent:-28.4px;letter-spacing:normal;font-family:&quot;arial&quot;,sans-serif;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;display:inline;white-space:normal;orphans:2;font-size-adjust:none;font-stretch:normal;float:none;">. &ZeroWidthSpace;</span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span></p><p style="line-height:150%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteFontFace-13" lang="EN-GB" style="line-height:150%;font-size:13px;">A4. Understand why do some countries achieve
high levels of economic development and others do not. </span></p><p style="text-align:justify;line-height:150%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteFontFace-13" lang="EN-GB" style="line-height:150%;font-size:13px;">A5. Understand the policies that
government can implement to change the growth path of their countries</span></p><p style="text-align:justify;line-height:150%;text-indent:-21.3pt;margin-left:21.3pt;"><span class="ms-rteFontFace-13" lang="EN-GB" style="line-height:150%;font-size:13px;"><br></span>&nbsp;</p>

<p><span class="ms-rteFontFace-13" style="font-size:13px;"><strong>&ZeroWidthSpace;</strong><span lang="EN-GB"><strong>B. Cognitive
skills&nbsp;</strong></span></span></p><p><span class="ms-rteFontFace-13" lang="EN-GB" style="font-size:13px;"><span lang="EN-GB">B1.
Learn how to think systematically and strategically about aspects of economic
development&nbsp;</span></span></p><span class="ms-rteFontFace-13" id="ms-rterangepaste-start" style="font-size:13px;"></span><p style="margin:0px 0px 10px;text-align:left;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13" style="font-size:13px;">B2. Reflect on and begin to critically evaluate the aspects that affect economic development.</span></p><p style="margin:0px 0px 10px;text-align:left;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13" style="font-size:13px;">B3. Use conceptual frameworks to describe economic development and economic development policies and what needs to be done to implement these policies and to achieve development; particularly for developing countries.&nbsp;<br></span></p><p><span class="ms-rteFontFace-13" style="font-size:13px;">B4. Critically evaluate theories in relation to economic development and international setting with which they are familiar and the relative standpoints of others within different contexts;&ZeroWidthSpace;</span></p><p><span class="ms-rteFontFace-13" style="font-size:13px;"><br></span>&nbsp;</p><p><span class="ms-rteFontFace-13" style="font-size:13px;"><span lang="EN-GB"><strong>C.
Practical and professional skills</strong></span></span><span class="ms-rteFontFace-13"><br></span></p><p style="margin:0px 0px 10px;text-align:left;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-size:13px;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13">C1. Evaluate the impact of economic development on the&nbsp; </span></p><p style="margin:0px 0px 10px;text-align:left;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-size:13px;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; country prosperity and international stand.&nbsp; </span></p><p style="margin:0px 0px 10px;text-align:left;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-size:13px;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13">C2. Demonstrate advanced professional and educational </span></p><p style="margin:0px 0px 10px;text-align:left;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-size:13px;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; capabilities using appropriate interpersonal, written </span></p><p style="margin:0px 0px 10px;text-align:left;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-size:13px;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; communication and critical thinking skills that are required&nbsp; </span></p><p style="margin:0px 0px 10px;text-align:left;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-size:13px;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for economic development policies</span></p><p style="margin:0px 0px 10px;text-align:left;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-size:13px;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13">.C3.&nbsp; Apply theories and concepts relevant to economic </span></p><p style="margin:0px 0px 10px;text-align:left;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-size:13px;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; development in all its dimension within local, regional and </span></p><p style="margin:0px 0px 10px;text-align:left;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-size:13px;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; international contexts.&nbsp;&nbsp; </span></p><p style="margin:0px 0px 10px;text-align:left;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-size:13px;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13">C4. Develop knowledge, skills, attitudes and values </span></p><p style="margin:0px 0px 10px;text-align:left;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-size:13px;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; necessary for economic development policies&nbsp; </span></p><p style="margin:0px 0px 10px;text-align:left;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-size:13px;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; implementation&nbsp; particularly in developing struggling <br></span></p><p style="margin:0px 0px 10px;text-align:left;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-size:13px;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; countries.&nbsp;</span></p><p style="margin:0px 0px 10px;text-align:left;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-size:13px;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13"><br></span>&nbsp;</p><p><span class="ms-rteFontFace-13" lang="EN-GB" style="font-size:13px;"><strong>D.
Key/transferable skills</strong></span></p><p style="margin:0px 0px 10px;text-align:justify;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13" style="font-size:13px;"><strong>D1.</strong>Be creative and assertive in presenting ideas related to economic development and economic development policies. </span></p><p style="margin:0px 0px 10px;text-align:justify;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13" style="font-size:13px;"><strong>D2</strong>.Articulate ideas and communicate effectively using appropriate theories pertinent to the concept of economic development in general and in particular economic development in developing countries. </span></p><p style="margin:0px 0px 10px;text-align:justify;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13" style="font-size:13px;"><strong>D3</strong>.Communicate effectively, using economic vocabulary, both orally and in writing&nbsp; and listen actively;</span></p><p style="margin:0px 0px 10px;text-align:justify;color:#444444;text-transform:none;line-height:1.6;text-indent:0px;letter-spacing:normal;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"><span class="ms-rteFontFace-13" style="font-size:13px;"><strong style="text-align:left;color:#444444;text-transform:none;text-indent:0px;letter-spacing:normal;font-style:normal;font-variant:normal;font-weight:700;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;">D4</strong><span style="text-align:left;color:#444444;text-transform:none;text-indent:0px;letter-spacing:normal;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;display:inline !important;white-space:normal;orphans:2;float:none;">.</span><span style="text-align:left;color:#444444;text-transform:none;text-indent:0px;letter-spacing:normal;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;display:inline;white-space:normal;orphans:2;float:none;">Conduct research into economic development issues related to the course topics, either individually or as part of a team for projects/dissertations/presentations. This requires familiarity with and an evaluative approach to a range of economic data, sources of information and appropriate methodologies, and for such to inform the overall learning process. </span><br></span></p><p><span style="font-size:13px;"><strong class="ms-rteFontFace-13" style="font-size:13px;">&ZeroWidthSpace;D5</strong><span class="ms-rteFontFace-13" style="font-size:13px;">.Self-reflection and criticality including self-awareness, openness and sensitivity to diversity in terms of various aspects related to and affecting economic development; particularly in developing countries</span><br></span></p><p><br>&nbsp;</p></td>
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
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_89">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_89" class="modal fade" role="dialog">
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
											<td>EL111 is three credit hour university requirements. It aims to develop in students the skills of listening, speaking, reading and writing in English, together with attention to function and correct use of vocabulary and grammar. The course introduces thematic topics which aim at developing critical thinking skills. In addition, learning strategies such as prior knowledge, scanning for specific information, skimming for main idea and getting meaning from context are emphasized.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;<br><br></p></td>
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
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_90">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_90" class="modal fade" role="dialog">
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
											<td>EL112 is an advanced integrated skills course which builds on knowledge gained from EL111. The course continues to develop the four communication skills of listening, speaking, reading and writing to a more advanced level. In addition, students start to write longer essays.</td>
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
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_96">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_96" class="modal fade" role="dialog">
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
											<td>This is a four-credit-hour module of one semester in length. The module aims to help students become better readers of English texts and build their vocabulary. It focuses on expanding students’ reading skills and vocabulary use so that they can cope with different academic, professional and social situations effectively. The course applies the Interactive Reading model where reading is an active process in which readers draw upon top-down processing (bringing meaning to the text), as well as bottom-up processing (decoding words and other details of language). The top-down aspect of this construct suggests that reading is facilitated by interesting and relevant reading materials that activate a range of knowledge in a reader's mind. This knowledge is refined and extended during the act of reading. The bottom-up aspect of this model suggests that the students need to pay attention to language proficiency, including vocabulary. As an academic reading course, it addresses the teaching of higher level reading strategies without neglecting the need for language support. In addition, it addresses both sides of the interactive model. High-interest academic readings and activities provide students with opportunities to draw upon authentic life experience in their mastery of a wide variety of reading strategies and skills, including
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
											<td><p>&ZeroWidthSpace;</p><p style="text-align:justify;"><em>The module aims to provide the learners with necessary skills trough:</em></p><p style="text-align:justify;">&nbsp;</p><p style="text-align:justify;">1. Providing the students with opportunities to draw upon life experience in their mastery of a wide variety of reading strategies and skills that include previewing, scanning, using contextual clues to get the meaning, finding the main idea, summarizing and making inferences.</p><p style="text-align:justify;">2. Improving the students' language proficiency and the students' ability to decode and process meaning.</p><p style="text-align:justify;">3. Helping the students become independent learners by taking the responsibility of building their own vocabulary repertoire</p><p style="text-align:justify;">4. Guiding the students to notice and effectively practice new vocabulary items as they encounter them.</p><p>5. Enhancing students' academic proficiency by highlighting the reciprocal relationship between reading comprehension and reflection writing.<br><br></p><p>&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p>&ZeroWidthSpace;</p><p style="text-align:justify;"><strong>A.</strong>&nbsp;&nbsp;&nbsp;<strong>Knowledge and understanding</strong></p><p style="text-align:justify;"><em>At the end of the module, learners will be expected to:</em></p><p style="text-align:justify;"><strong>A1.</strong>&nbsp;demonstrate understanding of any given reading passages by responding correctly to its tasks and activities individually or in groups.</p><p style="text-align:justify;"><strong>A2.</strong>&nbsp;show knowledge and understanding of the learned reading strategies.</p><p style="text-align:justify;"><strong>A3.</strong>&nbsp;show recognition of the various “meanings" of words to reach a better understanding of the context and the written word.</p><p style="text-align:justify;"><strong>A4.</strong>&nbsp;reveal awareness of appropriate language structures and vocabulary items suitable for different contexts and situations.</p><p style="text-align:justify;">&nbsp;</p><p><strong>B.</strong>&nbsp;&nbsp;&nbsp;<strong>Cognitive skills</strong><br><br><em>At the end of the module, learners will be expected to:</em><br><br><strong>B1.</strong>&nbsp;search for and collect specific data related to the topics under discussion.</p><p style="text-align:justify;"><strong>B2.</strong>&nbsp;draw conclusions for the discussed topics based on the collected data and analyzed information.</p><p style="text-align:justify;"><strong>B3.</strong>&nbsp;incorporate in writing the words learned in real life scenarios.</p><p style="text-align:justify;"><strong>B4</strong>. improve the analytical and critical thinking skills through the identification of possible “meanings".</p><p><strong>B5.</strong>&nbsp;analyze language functions used and identify useful language expressions.</p><p>&nbsp;</p><p><strong>C.</strong>&nbsp;&nbsp;&nbsp;<strong>Practical and professional skills</strong><br><br><em>At the end of the module, learners will be expected to:</em></p><p style="text-align:justify;"><strong>C1.</strong>&nbsp;communicate in English orally and in writing on diverse occasions.</p><p style="text-align:justify;">&nbsp;</p><p style="text-align:justify;"><strong>C2.</strong>&nbsp;identify problems in the given topics and provide creative solutions.</p><p style="text-align:justify;">&nbsp;</p><p style="text-align:justify;"><strong>C3.</strong>&nbsp;give oral presentations using power points, flipcharts, pictures, role plays, etc. to discuss what has been read orally.</p><p style="text-align:justify;">&nbsp;</p><p><strong>C4.</strong>&nbsp;assess the work done using self/peer-assessment.</p><p>&nbsp;</p><p><strong>D.</strong>&nbsp;&nbsp;&nbsp;<strong>&nbsp;</strong><strong>Key transferable skills</strong><br><br><strong>&nbsp;</strong></p><p style="text-align:justify;"><em>At the end of the module, learners will be expected to:</em><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></p><p style="text-align:justify;"><strong>D1.</strong>&nbsp;enrich vocabulary repertoire through exploring new assigned topics and writing on those topics</p><p style="text-align:justify;"><strong>D2.</strong>&nbsp;develop communicative confidence (as reader and writer)</p><p style="text-align:justify;"><strong>D3.</strong>&nbsp;discuss all posed topics, problems, provided solutions and drawn conclusions.</p><p><strong>D4.</strong>&nbsp;develop effective presentation skills that would enhance self-confidence.<br><br></p><p><br></p></td>
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
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_97">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_97" class="modal fade" role="dialog">
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
											<td>The course introduces the student to the basics of French. These include the alphabet, common everyday expressions, simple sentences, short dialogues and small paragraphs. The four skills of reading, writing, listening and speaking will be equally emphasized. However, as we live in the age of the image, students will have ample exposure to a variety of audio-visual material which boost their command of the language at the beginner’s level.  The communicative approach is to be adopted in face-to-face tutorials and the various methods of enabling students to learn on their own will be prioritized.</td>
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
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_98">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_98" class="modal fade" role="dialog">
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
											<td>The course builds on what the student has learnt in level (1). Toward this end, it introduces the student to more everyday expressions, more widely-used short sentences, some compound and complex sentences, medium-size dialogues, and short passages. While the skills of listening and speaking will be receiving adequate attention, more emphasis is to be placed on the skills of reading and writing.  Face-to-face tutorials will be communicative and students will be empowered to learn on their own.</td>
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
                    GR 117&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Empowerment of Women <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    This course focuses on empowering women and activating their role in leading political, economic and social development.

                </div>
				
				<div class="course-details float-right">
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_116">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_116" class="modal fade" role="dialog">
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
                    GR101&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Self-Learning Skills <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    GR101 focuses on developing self-learning skills. It prepares students for university studying and specifically time management, good study habits, critical and analytic thinking styles.
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
											<td>GR101 focuses on developing self-learning skills. It prepares students for university studying and specifically time management, good study habits, critical and analytic thinking styles.</td>
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
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_93">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_93" class="modal fade" role="dialog">
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
											<td><p>&ZeroWidthSpace;<br><br></p></td>
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
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_99">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_99" class="modal fade" role="dialog">
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
                    GR115&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Current International Affairs <span class="float-right">(3) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    GR115 examines current international concerns such as the interactions of civilizations, North and South relations, national and international civil societies, human rights and illegal immigration.

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
								<span class="modal-title">Current International Affairs</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>GR115</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Current International Affairs</td>
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
											<td>GR115 examines current international concerns such as the interactions of civilizations, North and South relations, national and international civil societies, human rights and illegal immigration.
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
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_115">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_115" class="modal fade" role="dialog">
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
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;<br></p><p>&ZeroWidthSpace;<br></p></td>
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
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_117">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_117" class="modal fade" role="dialog">
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
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_118">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_118" class="modal fade" role="dialog">
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
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_114">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_114" class="modal fade" role="dialog">
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
                    LB170&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Communication Skills for Business and Management <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Personal and corporate success in business relies on effective communication. Communication Skills for Business and Management will help you acquire skills to distinguish you from your peers. This key introductory Level 1 course is practical and will empower you to undertake more insightful case-study analysis, write successful essays, and produce powerful reports. From proposals to emails, you’ll work with a wide range of texts from business studies courses and the wider business world, deepening your knowledge and developing your written communication skills - helping you to succeed in both business studies and business generally. 
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
								<span class="modal-title">Communication Skills for Business and Management</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>LB170</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Communication Skills for Business and Management</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>EL 122: Intermediate English</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Personal and corporate success in business relies on effective communication. Communication Skills for Business and Management will help you acquire skills to distinguish you from your peers. This key introductory Level 1 course is practical and will empower you to undertake more insightful case-study analysis, write successful essays, and produce powerful reports. From proposals to emails, you’ll work with a wide range of texts from business studies courses and the wider business world, deepening your knowledge and developing your written communication skills - helping you to succeed in both business studies and business generally. </td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p><span class="ms-rteFontSize-2" id="ms-rterangepaste-start"></span><span lang="EN-GB" style="font-family:&quot;times new roman&quot;,serif;font-size:13px;">LB170’s design will be
relevant for students from OUBS Openings to Level 2 courses.&nbsp; Students’ confidence, performance and
progression potentials will be enhanced and ultimately academic standards will
be positively influenced as well as widening participation, retention and
completion rates.&nbsp;&nbsp; The emphasis in the
course is on processes and practices (the ‘skills’) of communication rather
than on content in a ‘traditional’ academic sense. As such the course reverses
the balance present in other OUBS courses where communication skills are fore
grounded but are always at the service of the course content and consequently
occupy a less significant position in the learning outcomes.&nbsp;&nbsp;&nbsp; The model of communication skill
development outlined above is a positive rather than a deficit model. It draws
on current thinking about literacy development in which a more traditional
skills development model which treats communication as an all-purpose set of
skills with universal application is overlain, firstly, with a model that
places literacy in context and sees literacy practices as situated within particular
spheres of activity (in this case, business, broadly, and business studies more
specifically). Secondly it draws on a model that highlights the ideological and
personal investment that come into play when individuals and organisations
engage in communicative acts.</span>&ZeroWidthSpace;&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>A. Knowledge
and understanding</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1: Can understand and use familiar everyday expressions and
Phrases aimed at the satisfaction of needs of a concrete type.The internal and
external factors affecting business organisations and their stakeholders. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2: understand sentences and frequently used expressions related
to areas of most immediate relevance in one’s major such as the operation and
management of the HR function of a business organisation. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3: Can produce clear, detailed text on a wide range of subjects
and explain a viewpoint on a topical issue giving the advantages and
disadvantages of various options.<span>&nbsp; </span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4: Can
understand a wide range of demanding, longer texts, and recognize implicit
meaning. Such as the operation and management of the marketing function of a
business organisation. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1 After studying the course, the student will have developed the
language they need to exercise the following thinking and communication skills
and have developed a critical perspective on this language in the light of a
range of alternative, available language and communication practices: </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: recognize, compare and contrast different ways of analysing
business case studies and other material about contemporary business practice. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3: apply their knowledge in the analysis of practical business
problems and issues. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B4: recognize, compare and contrast different interpretations of
and approaches to practical business problems and issues. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: analyse work-related cases and situations to identify problems
in the organization and management of a functional area. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: identify and communicate potential solutions based on
knowledge of theory and apply it to their own work situation.<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3: related the communication skills needed for academic study to
those needed in the workplace. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Read and précis written text materials for key salient points.
</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2:<span>&nbsp; </span>communicate effectively
in writing, showing recognition of audience and purpose. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D3: select data, information and ideas from different sources and
present in an appropriate fashion to support an argument. </span></p>

<span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;font-size:13px;">D4: identify some of the
key strengths and needs of their own communication skills development and
identify opportunities to address these in the light of their critique of the
language and literacy practices they have encountered.</span><br></td>
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
                    MKT331&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Digital Marketing <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The proliferation of the internet across the globe has increased the use of mobile internet devices, tablets, smart phones etc., and improved customer reach, therefore increasing the importance and relevancy of E-marketing for marketing managers.  The internet produced many interesting and innovative methods to offer better customer value. This includes Web sites for marketing communication and customer support; one-to-one communication to many different receiving devices; and consumer behavior insights based on offline and online data combination and inventory optimization through CRM-SCM integration. More recently the development of different social media outlets provided perfect platforms for connecting with today’s consumer: High readership blogs, social networks (such as Facebook and LinkedIn), and online communities (such as YouTube, Twitter and Second Life). Such mediums offer consumers in groups a platform to voice their needs, concerns, and feedback. Intelligent marketers have learned how to take advantage of the great access enabled through social media to improve their products and marketing communication. Today, a balanced and effective marketing strategy must rely greatly upon- online marketing and social media.  
 
Electronic Marketing (E- Marketing) involves the use of electronic means to reach marketing objectives. Since the 1980s, this has included database marketing, Customer Relationship Management, and loyalty programs. In addition, the increased reliance of consumers on the internet for their purchases and for information gathering has transformed the direction towards online marketing and social media strategy. 
 
In this course, students get an introduction to the fundamental principles of online marketing (e marketing and social-media) both with theory and with practical trainings. Students will build upon pre-acquired knowledge from other marketing courses.   

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
								<span class="modal-title">Digital Marketing</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>MKT331</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Digital Marketing</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B 120: An Introduction to Business Study</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>The proliferation of the internet across the globe has increased the use of mobile internet devices, tablets, smart phones etc., and improved customer reach, therefore increasing the importance and relevancy of E-marketing for marketing managers.  The internet produced many interesting and innovative methods to offer better customer value. This includes Web sites for marketing communication and customer support; one-to-one communication to many different receiving devices; and consumer behavior insights based on offline and online data combination and inventory optimization through CRM-SCM integration. More recently the development of different social media outlets provided perfect platforms for connecting with today’s consumer: High readership blogs, social networks (such as Facebook and LinkedIn), and online communities (such as YouTube, Twitter and Second Life). Such mediums offer consumers in groups a platform to voice their needs, concerns, and feedback. Intelligent marketers have learned how to take advantage of the great access enabled through social media to improve their products and marketing communication. Today, a balanced and effective marketing strategy must rely greatly upon- online marketing and social media.  
 
Electronic Marketing (E- Marketing) involves the use of electronic means to reach marketing objectives. Since the 1980s, this has included database marketing, Customer Relationship Management, and loyalty programs. In addition, the increased reliance of consumers on the internet for their purchases and for information gathering has transformed the direction towards online marketing and social media strategy. 
 
In this course, students get an introduction to the fundamental principles of online marketing (e marketing and social-media) both with theory and with practical trainings. Students will build upon pre-acquired knowledge from other marketing courses.   
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td>&ZeroWidthSpace;&ZeroWidthSpace;This is a compulsory module in the Marketing track. This course provides students with a comprehensive introduction into the field of online marketing. It is designed in a way, which builds on students' pre-existing knowledge in general marketing management to elaborate the concepts of digital marketing. After completing this course students should be able to: <p>&nbsp;</p><ul><li>Understand the nature and concepts of online marketing and apply online marketing tools, instruments and principles through theory and case studies. </li><li>Understand the importance of online marketing and social media to a company's' overall marketing plan in contemporary marketing. </li><li>Understand internet users and identify profitable E-Marketing strategies.</li><li>Understand the design and evaluation of multimedia applications for marketing strategy.&nbsp; </li><li>Review current practices in electronic marketing.  Understand the marketing effectiveness of web-based marketing approaches. </li><li>Learn how to use the internet as a research method and learn and practice how to publish information on the internet. </li><li>Be able to develop effective strategies for generating traffic, optimizing conversion, achieving customer satisfaction, optimizing profitability, generating social media strategies and continuous innovation within online marketing environment. </li><li>Understand the E-Marketing context: e-business models, performance metrics, and role of strategic planning. </li><li>Describe E-marketing strategies of segmenting, targeting, positioning, and differentiation.</li><li>Know how to use marketing functions of product, pricing, distribution, and marketing communication for a firm's E-Marketing strategy.&ZeroWidthSpace;&ZeroWidthSpace;<br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&ZeroWidthSpace;<strong>A. Knowledge
and understanding</strong></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1: Evaluate
the role and implications of digital methods within marketing.&nbsp; </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2: Evaluate
examples of contemporary electronic marketing methods such as microsites and
banner ads and compare them to conventional approaches.&nbsp; </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3:
Appreciate the marketing implications of the design and application of
multimedia/Web based products and evaluate them from an e- marketing
perspective.&nbsp; </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4: Evaluate
the advantages and limitations of different approaches to Web based marketing
including text and information based pages, virtual worlds, interactive
graphics and animation&nbsp; </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A5: Evaluate
the impact of web based innovations on marketing and consumer behavior. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A6: Consider
the impact that modern technology has (Internet, social media, etc.) on
marketing innovation. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A7: Consider
what new ways of thinking are needed in E-marketing </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: Use critical analysis to evaluate e-marketing tactics within a
business perspective </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: Provide a theoretical and practical basis for critically
assessing the range of e-marketing tools as well as their advantages and
disadvantages </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3: Explore the impact of online communities and evaluate their
uses in E-marketing. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B4: Evaluate the utility of concepts, tools and frameworks to
solve ebusiness problems. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B5: Evaluate the advantages and limitations of virtual worlds,
interactive graphics, animations and social media. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B6: Evaluate the impact of digital marketing strategies on
consumer decision making.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: Have developed market awareness of E-marketing issues&nbsp; </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Analyse e-marketing cases and identify organizational
challenges in developing responses relevant to the environment. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3: Apply course concepts to students’ own interactions with
organisations and life experiences. C4: Build upon important workplace skills
(e.g. cooperative, teamwork, meeting deadlines, report writing) through
cooperative learning activities </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C5: Appreciate multicultural influences on the e-marketplace, on
ebusiness ethics, and on socially responsible E-marketing. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D Key transferable skills </strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Make Decisions and solve problems in a viable approach
engaging with data analysis, interpretation and extrapolation. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2: Work independently, communicate effectively, planning,
monitoring, reflecting on and improving their own learning. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D3: Find, assess and apply information from a variety of sources,
using information technology where necessary Immerse in related information,
arguments and ideas.<span> &nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>D4: Identify some of the key strengths and needs of their own learning and identify opportunities to address these.&ZeroWidthSpace;</span></span></p></td>
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
                    MKT332&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Service Marketing <span class="float-right">(4) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    The services sector is gaining increased importance as a contributor to GDP and employment growth in both developed and developing countries. Developments in information technology and innovation are leading to the creation of new services and opportunities continuously, to offer better value to clients and at affordable prices. In addition, organizations from all sectors  
 
including technological and industrial are realizing the importance of providing distinguished quality services to gain competitive advantage. Consequently, learning about services marketing has become essential despite the sector of employment one chooses to follow, since services have infiltrated the world around us.  The majority of business activity today relates to services. This has changed the marketing worldview. This module builds on the concepts covered in the basic marketing courses. It addresses the distinctive challenges integral to the marketing of services in a variety of modern business  
 
Settings emphasis on distinctive features of service management and marketing, in addition to the theories, instruments, and strategies required to tackle them. Aspects of relationship marketing and the new service‐dominant logic of marketing will also be covered.

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
								<span class="modal-title">Service Marketing</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>MKT332</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Service Marketing</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B324</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>4</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>The services sector is gaining increased importance as a contributor to GDP and employment growth in both developed and developing countries. Developments in information technology and innovation are leading to the creation of new services and opportunities continuously, to offer better value to clients and at affordable prices. In addition, organizations from all sectors  
 
including technological and industrial are realizing the importance of providing distinguished quality services to gain competitive advantage. Consequently, learning about services marketing has become essential despite the sector of employment one chooses to follow, since services have infiltrated the world around us.  The majority of business activity today relates to services. This has changed the marketing worldview. This module builds on the concepts covered in the basic marketing courses. It addresses the distinctive challenges integral to the marketing of services in a variety of modern business  
 
Settings emphasis on distinctive features of service management and marketing, in addition to the theories, instruments, and strategies required to tackle them. Aspects of relationship marketing and the new service‐dominant logic of marketing will also be covered.
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p>&ZeroWidthSpace;&ZeroWidthSpace;This is a compulsory module in the marketing track. The module is designed to give learners a broad understanding of the key concepts and business practices in service marketing. The module provides an overview of the nature and scope of services marketing and its role in achieving business objectives. The module aims to: <br></p><ul><li>Provide learners with a clear understanding of the concepts and business functions of services marketing&nbsp; </li><li>Give learners an overview of the environmental factors which influence services marketing decisions</li><li>Introduce learners to the need to develop an appropriate services marketing mix and identify and analyze the various components of the services marketing mix </li><li>Familiarize learners with the role of marketing to service providers. </li><li>Appreciate the challenges embedded in marketing and managing services and study the tools and processes to respond to these challenges. </li><li>Evaluate the key issues required in managing customer satisfaction and service quality </li><li>Appreciate the role of employees and customers in service delivery, customer satisfaction and service quality.&nbsp;</li><li>Understand the critical aspects of service businesses such as managing supply and demand, relationship management, and the overlap in marketing/operations/human resource systems. &ZeroWidthSpace;<br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><b>&ZeroWidthSpace;<span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A. Knowledge
and understanding</span></b><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1.
Differentiate between product and service characteristics, and know how this
can be used to establish competitive advantage for a firm. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2.
Understand why the application of the marketing mix in a service environment is
built up from the interaction between customers and their suppliers. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3. Develop
an understanding of the links between the service providers (people), the
procedures (processes), and the physical evidence of the service offering. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4.
Understand service quality management as the basis for developing customer
satisfaction and develop skills in service quality problem diagnosis and
service improvement. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A5.
Understand the importance of customer retention, service recovery, relationship
development, and the role of internal marketing. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A6. Consider
the impact that modern technology has (Internet, social media, etc.) on
service(s) marketing innovation. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A7. Consider
what new ways of marketing thinking are needed in service dominant modern
economies.</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1. Use critical analysis to perceive service shortcomings in
reference to create service excellence;<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2. Provide a theoretical and practical basis for assessing
service performance using company examples;<span>&nbsp;
</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3. Identify and discuss characteristics and challenges of
managing service firms in the modern world using cultural implications;<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B4. Discuss key linkages between marketing and other business
functions in the context of designing and operating an effective service
system.<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B5. Explain the unique challenges of services marketing, including
the elements of product, price, place, promotion, processes, physical evidence,
and people.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: Integrate course concepts into individual performance to
become better customer service representatives in the service environment. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Analyse work-related cases and situations and identify
organizational challenges in developing responses related to the environment. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3: Apply course concepts to students’ own interactions with
organisations and life experiences. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C4: Build upon important workplace skills (e.g. cooperative,
teamwork, meeting deadlines, report writing) through cooperative learning
activities </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C5: Discuss the influences of the multicultural marketplace,
business ethics, and socially responsible marketing on services marketing </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C6: Describe how customer relationship marketing (CRM), including
retention strategies, creates an environment that achieves excellence in
customer service</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&ZeroWidthSpace;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Make Decisions and solve problems in a viable approach
engaging with data analysis, interpretation and extrapolation. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2: Work independently, communicate effectively, planning,
monitoring, reflecting on and improving their own learning</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D3: Find, assess and apply information from a variety of sources,
using information technology where necessary Immerse in related information,
arguments and ideas.</span><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span><span style="text-align:left;color:#444444;text-transform:none;text-indent:0px;letter-spacing:normal;font-size:13px;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;white-space:normal;orphans:2;"></span><span style="text-align:left;color:#444444;text-transform:none;text-indent:0px;letter-spacing:normal;font-size:11pt;font-style:normal;font-variant:normal;font-weight:400;text-decoration:none;word-spacing:0px;display:inline;white-space:normal;orphans:2;float:none;">D4: Identify some of the
key strengths and needs of their own learning and identify opportunities to
address these</span></span></span></p><br></td>
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
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_101">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_101" class="modal fade" role="dialog">
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
											<td>The course introduces the student to the basics of Spanish. These include the alphabet, common everyday expressions, simple sentences, short dialogues and small paragraphs. The four skills of reading, writing, listening and speaking will be equally emphasized. However, as we live in the age of the image, students will have ample exposure to a variety of audio-visual material which boost their command of the language at the beginner’s level. The communicative approach is to be adopted in face-to-face tutorials and the various methods of enabling students to learn on their own will be prioritized.</td>
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
                    <a class="btn btn-sm" href="#" data-toggle="modal" data-target="#modal_102">View More Details</a>
                </div>
				
				<div class="clear"></div>
				
				<!-- Modal -->
				<div id="modal_102" class="modal fade" role="dialog">
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
											<td>The course builds on what the student has learnt in level (1). Toward this end, it introduces the student to more everyday expressions, more widely-used short sentences, some compound and complex sentences, medium-size dialogues, and short passages. While the skills of listening and speaking will be receiving adequate attention, more emphasis is to be placed on the skills of reading and writing. Face-to-face tutorials will be communicative and students will be empowered to learn on their own.</td>
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
                    SYS210&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Managing Technologies and Innovation <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Technology plays a significant and invaluable role in the different aspects of human societies. It is a key resource of profound importance for a nation’s security and economic development. In addition, it is viewed as an important strategic factor and fundamental element for economic growth and as an instrumental means of controlling nature and resources. It also exerts a powerful influence on standards of living and quality of life. New knowledge, innovations and professional skills are an intrinsic part of new technology. Because technology is continuously changing, with new processes and products being developed or improved regularly, the need to manage technology is also continuous, and one that grows with the expansion of economic activities. Management of technology is a difficult and complex process, but it is an issue that faces all firms today. It involves the handling of technical and social issues in a broad spectrum of functional areas including manufacturing, design, development, information, processing, construction, pollution, violence, and so forth. Management of technology and innovation is concerned with developing and enhancing the capabilities of individuals and the characteristics of institutions to match the potential benefits, to contain the hazards resulting from technological change and also to find new ways to compete and survive. The role of MTI (Managing Technology and Innovation) is to ensure the proper execution of the following functions: 
   Selection of technology, or rather technological products 
   Effective negotiation and contracting for their acquisition 
   To integrate strategy and technology 
   Adaptation to local conditions (environmental, human, etc.). 
   Insights into MTI (Managing Technology and Innovation)

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
								<span class="modal-title">Managing Technologies and Innovation</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>SYS210</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Managing Technologies and Innovation</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B123</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Technology plays a significant and invaluable role in the different aspects of human societies. It is a key resource of profound importance for a nation’s security and economic development. In addition, it is viewed as an important strategic factor and fundamental element for economic growth and as an instrumental means of controlling nature and resources. It also exerts a powerful influence on standards of living and quality of life. New knowledge, innovations and professional skills are an intrinsic part of new technology. Because technology is continuously changing, with new processes and products being developed or improved regularly, the need to manage technology is also continuous, and one that grows with the expansion of economic activities. Management of technology is a difficult and complex process, but it is an issue that faces all firms today. It involves the handling of technical and social issues in a broad spectrum of functional areas including manufacturing, design, development, information, processing, construction, pollution, violence, and so forth. Management of technology and innovation is concerned with developing and enhancing the capabilities of individuals and the characteristics of institutions to match the potential benefits, to contain the hazards resulting from technological change and also to find new ways to compete and survive. The role of MTI (Managing Technology and Innovation) is to ensure the proper execution of the following functions: 
   Selection of technology, or rather technological products 
   Effective negotiation and contracting for their acquisition 
   To integrate strategy and technology 
   Adaptation to local conditions (environmental, human, etc.). 
   Insights into MTI (Managing Technology and Innovation)
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><span lang="EN-GB">&ZeroWidthSpace;The aim of this
module, after accomplishing both parts of it, is to familiarize students with
an integrative approach to the management of technology and innovation.<span>&nbsp; </span>It introduces the concept of MTI and examines
internal innovation planning, implementation and evaluation and control. It
also introduces building the capabilities necessary for MTI success.<span>&nbsp; </span></span><p style="text-align:justify;"><span lang="EN-GB">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB">At the end of
both parts of the module, students are expected to attain the following
objectives: </span></p><p style="margin:6pt 0in 0pt 20.9pt;text-align:justify;line-height:115%;"><span lang="EN-GB">Understand the significance of technology, innovation and their
management </span></p><p style="margin:6pt 0in 0pt 20.9pt;text-align:justify;line-height:115%;"><span lang="EN-GB">Identify the key MTI concerns in strategy </span></p><p style="margin:6pt 0in 0pt 20.9pt;text-align:justify;line-height:115%;"><span lang="EN-GB">Understand both product and process innovation<span>&nbsp;&nbsp; </span></span></p><p style="margin:6pt 0in 0pt 20.9pt;text-align:justify;line-height:115%;"><span lang="EN-GB">Recognize the foundations of internal innovation and its
implementation </span></p><p style="margin:6pt 0in 0pt 20.9pt;text-align:justify;line-height:115%;"><span lang="EN-GB">Determine if the firm has achieved the desired outcomes and design a
proper tool for evaluation and control</span></p><p style="margin:6pt 0in 0pt 20.9pt;text-align:justify;line-height:115%;"><span lang="EN-GB">Identify elements for planning for acquiring, implementing and
evaluating technology </span></p><p style="margin:6pt 0in 0pt 20.9pt;text-align:justify;line-height:115%;"><span lang="EN-GB">Understand the core capabilities for a sustainable competitive
advantage </span></p><p style="margin:6pt 0in 0pt 20.9pt;text-align:justify;line-height:115%;"><span lang="EN-GB">Determine what information the firm actually has and to turn this
information into knowledge<span> &nbsp;&nbsp;</span></span></p><p style="margin:6pt 0in 0pt 20.9pt;text-align:justify;line-height:115%;"><span lang="EN-GB" style="font-family:ody;font-size:13px;">&nbsp;&nbsp;</span></p><span style="font-family:ody;font-size:13px;">

</span><span lang="EN-GB" style="font-family:ody;font-size:13px;">The course will prepare students with practical
skills through numerous realistic settings that are in line with the Quality
Assurance Agency’s benchmark statement expectations for business studies. It
also aims to enhance employability as the curriculum is of benefit to students
in the employment market and also relevant to many studying for their own
personal development. In so doing, the course provides students with a clear
understanding and appreciation of innovation dynamics both within and across
firm’s boundaries. By drawing from state of the art innovation literatures as
well as the extensive use of in-depth case study materials, the course analyses
opportunities and challenges related to creating, sustaining , managing
innovation and most of all integrating strategy and technology, with a specific
focus on technology-based organizations.</span>&ZeroWidthSpace;<p>&ZeroWidthSpace;<br></p></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><b>&ZeroWidthSpace;A. Knowledge
and understanding</b></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1:
Understand how organisations manage the internal process of innovation,
including effective search and knowledge acquisition, implementation, learning
and re–innovation </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2:
Appreciate the links between Innovation and competitive advantage, the different
kinds of innovations (radical vs. incremental, continuous vs. discontinuous,
etc.) </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3:
Understand innovation as a core business process and how it can be managed. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4:
Information gathering, Analyzing the external environment using management
models </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A5:
Conducting proper evaluation and control in innovation </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: Develop an awareness of the range, scope, and complexity of
the issues and problems related to the strategic management of technology and
innovation. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: Develop an understanding of the “state of the art’ of the
strategic management of technology and innovation. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3: Expose students to tools and concepts used by organisations
engaged in technology intensive industries. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B4: Designing Organizational structure based on the degree of
innovation needed B5: Develop appropriate capabilities for a sustainable
competitive advantage</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: Learn the basic skills necessary to construct a technology
strategy for an organisation. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Offer some practice in defining and working out strategic
management problems related to technological innovation and corporate
entrepreneurship. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3: Develop skills in leadership and engagement for a proper
implementation of an innovation strategy </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Effective communication, both orally and in writing, of
information, arguments and ideas, using language and styles appropriate for a
business context and audience. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2:<span>&nbsp; </span>Problem-solving and
decision-making using appropriate quantitative and qualitative skills including
data analysis, interpretation and extrapolation. </span></p>

<span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;font-size:13px;">D3:&nbsp; Effective performance in a team environment
both in face-to-face and/or virtual contexts. D4: self-appraisal and reflective
thinking in the areas of creativity, teamwork, leadership, career selection.</span><br></td>
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
                    SYS280&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Principles and Practice of Systems’ Thinking <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Traditionally, problems are frequently tackled by employing simple and convenient methods to achieve simple solutions. Such simple and popular approaches are not effective in solving complex, dynamic and diverse problems.  Regardless of the preliminary seemingly simple and easy application, the emphasis seems to be on the elements of the problem, rather than the “bigger picture”. Thus, no attention is given to the interaction between the elements, with the belief that there is one best solution.  As program failures intensify there is a growing need to develop and generate improved outcomes through systems thinking.  Systems’ thinking is a discipline of seeing the “whole”, recognizing patterns and interrelationships, and learning how to innovate a more effective, efficient and creative system/holistic solution(s).  
 
Holistic Systems Thinking considers the interdependent, inter-relational, and contextual aspects of phenomena and applies an integrated, inclusive mindset to problem solving.  Holistic approaches are preoccupied with the assumptions, knowledge, methods, and implications of various disciplines and treats them as an integrated whole, or system. Systems can be ecological, social, institutional, or a combination of all three, and relationships, within and between systems are recognized as complex with cyclical interdependencies, or  feedbacks. Higher-order, or emergent, properties become evident when systems are considered in this integrated fashion. 
 
A holistic systems world-view is grounded in people taking responsibility for their own actions and being receptive to transformational change. Fundamental to this philosophy are personal beliefs that sustainability is a conscious choice by people to aspire to a purposeful and equitable integration of a systems view of life. Holism can be referred to using different terminology including ecological systems thinking, and ‘joined-up’ mindset. 
 
This course will acquaint students with the basic concepts of systems thinking.  The primary emphasis will be the introduction of basic systems thinking fundamentals, i.e. defining a systems perspective about any situation or problem, solving problems with that perspective, drawing appropriate diagrams to illustrate the problem, describing and modeling a problem, and designing and improving upon system solutions.  

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
								<span class="modal-title">Principles and Practice of Systems’ Thinking</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>SYS280</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Principles and Practice of Systems’ Thinking</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>B207B</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Traditionally, problems are frequently tackled by employing simple and convenient methods to achieve simple solutions. Such simple and popular approaches are not effective in solving complex, dynamic and diverse problems.  Regardless of the preliminary seemingly simple and easy application, the emphasis seems to be on the elements of the problem, rather than the “bigger picture”. Thus, no attention is given to the interaction between the elements, with the belief that there is one best solution.  As program failures intensify there is a growing need to develop and generate improved outcomes through systems thinking.  Systems’ thinking is a discipline of seeing the “whole”, recognizing patterns and interrelationships, and learning how to innovate a more effective, efficient and creative system/holistic solution(s).  
 
Holistic Systems Thinking considers the interdependent, inter-relational, and contextual aspects of phenomena and applies an integrated, inclusive mindset to problem solving.  Holistic approaches are preoccupied with the assumptions, knowledge, methods, and implications of various disciplines and treats them as an integrated whole, or system. Systems can be ecological, social, institutional, or a combination of all three, and relationships, within and between systems are recognized as complex with cyclical interdependencies, or  feedbacks. Higher-order, or emergent, properties become evident when systems are considered in this integrated fashion. 
 
A holistic systems world-view is grounded in people taking responsibility for their own actions and being receptive to transformational change. Fundamental to this philosophy are personal beliefs that sustainability is a conscious choice by people to aspire to a purposeful and equitable integration of a systems view of life. Holism can be referred to using different terminology including ecological systems thinking, and ‘joined-up’ mindset. 
 
This course will acquaint students with the basic concepts of systems thinking.  The primary emphasis will be the introduction of basic systems thinking fundamentals, i.e. defining a systems perspective about any situation or problem, solving problems with that perspective, drawing appropriate diagrams to illustrate the problem, describing and modeling a problem, and designing and improving upon system solutions.  
</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><p style="text-align:justify;">&ZeroWidthSpace;&ZeroWidthSpace;SYS280 is a compulsory course in Business Studies/Systems' track.&nbsp; Systems thinking is an inquiry-based method of learning that uses the technique of perspective-taking, fosters holistic thinking, and engages in belief-testing. Systems theory identifies and analyzes the linkages among various elements in a system. For those new to systems theory, it is important to note that “systems" is plural. Thus, systems theory does not presume that there is one grand system to be studied. One intellectual thread of systems theory is the field of systems thinking. Systems thinking is a methodology for understanding and managing complex feedback systems such as the ones at work in business and other social systems. Systems thinking uses mapping of interrelationships as a mean to improve decision-maker understanding of how to intervene and improve system performance.&nbsp; <br></p><p style="text-align:justify;">Understanding the interworking of a system, or the relationships between the various actors of a system, is useful because it improves understanding of the outcomes of the system. For example, to understand why communities experience traffic congestion in a road system despite extensive road building requires an understanding of the relationships between the actors in the system. Students must understand how governments decide where to build or expand roads and how individuals select driving routes. If a government widens a congested road, it is likely to become congested again even if the destinations of current drivers, employment patterns, location of entertainment and service venues, and other determinants of driving patterns have not changed. The systems thinking approach builds theories for how the system works and uses them to develop insights about the behavior of the system over time, with the goal of improving system performance. The primary tools of systems thinking include system diagramming.&nbsp; </p><p style="text-align:justify;">After completing this course student will have opportunities to conduct inquire into, and represent their learning about holistic systems. Learning objectives might include: </p><ul><li>Provide an overview of the history, research and perspectives into systems thinking. </li><li>Understand and document system thinking objectives. </li><li>Demonstrate a capacity to appreciate that all actions have consequences within, between and among systems. </li><li>Establish a basic understanding of systems thinking terminology, theories, processes, methods, language and tools. </li><li>Understand how tipping points, interdependencies, feedback loops, and emergent properties impact a variety of social, economic and ecological systems. </li><li>Describe and model solutions that will enable system thinking ex. (mind maps, feedback &amp; causal loops, behavior over time diagrams, etc.) </li><li>Apply systems analysis to various problems (socio - technical, supply chain, value chain / lean, etc.). </li><li>Comprehend systemic limits such as carrying capacity and the ways humans can and do impact ecological systems. </li><li>Develop a set of diagramming techniques. This help in exploring your perceptions and understanding of a situation and in communicating this understanding to others. Specifically, you will:<br></li><li>Recognize how diagrams can be used to support thinking about complex situations.<br></li><li>Understand how diagrams can be used to develop and represent systems of interest within a complex situation.&nbsp;</li><li>Know the main types of diagrams which are most frequently used in systems thinking and practice, the purpose they serve and the conventions they use.&ZeroWidthSpace;&ZeroWidthSpace;<br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><b>A. Knowledge
and understanding</b></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1:<span>&nbsp; </span>Systemic thinking and the systems concepts
and language. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2: The
various ways to think about the messes they are analyzing, helping them
understand one another, appreciate one another’s viewpoints and reduce
conflicts and misapprehensions. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3: How they
might function more effectively in a group by improving their working
relationships. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4: Different
diagrams that are mostly used in systems thinking and practice.<span>&nbsp; </span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><span>&nbsp;</span><span>&nbsp;</span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1: Critically assess the differences between being a manager and
a systems practitioner.<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2: Better think about their relationships with others and thus
better understand the dynamics of these relationships.<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3. Develop a mentality to work as systems practitioners </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B4. Recognize the importance of building explicit and implicit
models and drawing diagrams to facilitate the understanding of complex
situations. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1: Learn how to learn and reflect on their learning journey.<span>&nbsp;&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2: Develop techniques and practical skills that can often help to
improve relationships and understandings with other people. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3: Develop teamwork and leadership skills</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C4: Become a systems thinker and practitioner who is able to link
theory to practice focusing on the context.<span>&nbsp;
</span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1: Better handle complex and messy situations. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2: Develop their learning abilities and reflection skills </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D3: Hone their critical and systemic skills and thus be able to
have a helicopter view of each situation and thus better understand it and
better cope with it. </span></p>

<span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;font-size:13px;">D4: Understand people
and some aspects of organizational behaviour.</span><br></td>
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
                    SYS380&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Managing Systems Complexity <span class="float-right">(8) Credit Hours</span>
                    <div class="clear"></div>
                </div>
                <div class="course-desc">
                    Engage students  with an awareness of the issues involved in managing change, moving them beyond "one-best way" approaches and providing them with access to multiple perspectives that they can draw upon in order to enhance their success in producing organizational change. These multiple perspectives provide a theme for the text as well as a framework for the way each chapter outlines different options open to managers in helping them to identify, in a reflective way, the actions and choices open to them. Multiple perspectives ensure that change managers are not trapped by a "one-best way" of approaching change that limits their options for action. Changing organizations is as messy as it is exhilarating, as frustrating as it is satisfying, as muddling-through and creative a process as it is a rational one. The module provides the student with an exploration into the tensions for those involved in managing organizational change. Rather than pretend that they do not exist it confronts them head on, identifying why they are there, how they can be managed and the limits they create for what the manager of organizational change can achieve.


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
								<span class="modal-title">Managing Systems Complexity</span>
								<button type="button" class="close" data-dismiss="modal">×</button>
							</div>
							<div class="modal-body">
								<table class="table table-striped">
									<tbody>
										<tr>
											<td>Course Code</td>
											<td>SYS380</td>
										</tr>
										<tr>
											<td>Course Title</td>
											<td>Managing Systems Complexity</td>
										</tr>
										<tr>
											<td>Pre-requisite</td>
											<td>SYS280</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>8</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>Engage students  with an awareness of the issues involved in managing change, moving them beyond "one-best way" approaches and providing them with access to multiple perspectives that they can draw upon in order to enhance their success in producing organizational change. These multiple perspectives provide a theme for the text as well as a framework for the way each chapter outlines different options open to managers in helping them to identify, in a reflective way, the actions and choices open to them. Multiple perspectives ensure that change managers are not trapped by a "one-best way" of approaching change that limits their options for action. Changing organizations is as messy as it is exhilarating, as frustrating as it is satisfying, as muddling-through and creative a process as it is a rational one. The module provides the student with an exploration into the tensions for those involved in managing organizational change. Rather than pretend that they do not exist it confronts them head on, identifying why they are there, how they can be managed and the limits they create for what the manager of organizational change can achieve.

</td>
										</tr>
										<tr>
											<td>Course Objectives</td>
											<td><ul><li>Develop students with &nbsp;a multiple perspectives approach to managing change</li><li>Recognizes the variety of strategies to facilitate change interventions </li><li>Reinforce students approach for the need for a tailored and creative approach to fit different contexts</li><li>Introduce the student to new and emerging trends, developments, themes, debates, and practices in organizational development and change interventions<br><br></li></ul></td>
										</tr>
										<tr>
											<td>Course Outcomes</td>
											<td><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><b>A. Knowledge
and understanding</b></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A1. Modern
trends in information systems and systems practice&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A2. The key concepts of
software development and maintenance, including principles of design, and the
representation and meaning of data<span> &nbsp;</span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A3.
Systemic methods of analysis, based on diagramming, modelling and other tools,
and how these can be used to improve computing practice and management decision
making<span>&nbsp; </span></span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">A4. The range
of situations in which information systems are used, the ways in which people
interact with them and the ethical, social and legal problems that information
systems can create. </span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p style="text-align:justify;"><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>B. Cognitive
skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B1. Apply systems thinking to academic literature and to
organisations, identifying suitable areas for systemic analysis and
appreciating the technical, economic and other factors at work<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B2. Analyse complex systems, and design and evaluate strategies or
software solutions for improving them<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B3. Describe, compare and contrast a variety of methods and tools,
identifying the best choices and applying them to specific problems<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B4. Develop and apply suitable analytical and management
techniques<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">B5. Explain the various roles, functions and interactions of
Members of a workplace team. </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>C. Practical and professional skills</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C1. Design, test and evaluate information systems </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C2. Use modern approaches and tools </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C3. Identify and handle the ethical, social and legal issues that
may arise during the design and use of information systems </span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">C4. Use diagramming and modelling tools to analyse complex
Systems.</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">&nbsp;</span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;"><strong>D. Key transferable skills.</strong></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D1. Work independently, planning, monitoring, reflecting on and
improving their own learning<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D2. Work in a group, communicating effectively<span>&nbsp; </span></span></p><p><span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;">D3. Find, assess and apply information from a variety of sources,
using information technology where necessary<span>&nbsp;
</span></span></p>

<span lang="EN-GB" style="font-family:&quot;calibri&quot;,sans-serif;font-size:13px;">D4. Use numerical and
analytical techniques to solve problems.</span><br></td>
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
                    TU170 introduces students to the essential concepts related to using computers with confidence. This is a fundamental course that familiarizes students with basic concepts of information technology, internet and web. The course also introduces students to practical skills for using computers as well as basic software and hardware applications.
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
											<td>EF003</td>
										</tr>
										<tr>
											<td>Credit Hours</td>
											<td>3</td>
										</tr>
										<tr>
											<td>Course Description</td>
											<td>TU170 introduces students to the essential concepts related to using computers with confidence. This is a fundamental course that familiarizes students with basic concepts of information technology, internet and web. The course also introduces students to practical skills for using computers as well as basic software and hardware applications.</td>
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

        
</div>
"""
soup = BeautifulSoup(html_content, "html.parser")

# List to store course details
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
    course_desc = item.find("div", class_="course-desc").get_text(strip=True).replace('\n', ' ').strip()
    course['course_desc'] = course_desc

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
                    value = cols[1].get_text(strip=True).replace('\n', ' ').strip()
                    course[key] = value

    # Keep only the fields defined in the headers
    course_filtered = {key: course.get(key, '') for key in
                       ["course_code", "course_title", "credit_hours", "course_desc", "pre-requisite",
                        "course_objectives", "course_outcomes"]}

    courses.append(course_filtered)

# Specify the CSV file name
csv_file = "scrappedCoursesBusiness.csv"

# Define the header for the CSV
headers = ["course_code", "course_title", "credit_hours", "course_desc", "pre-requisite", "course_objectives",
           "course_outcomes"]

# Write the data to CSV
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for course in courses:
        writer.writerow(course)

print(f"Data has been written to {csv_file}")
