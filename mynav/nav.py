from django.core.urlresolvers import reverse
#from mycoach import urls

def main_nav(user, selected):
    
    see_from_listA  = ['coaches', 'student_view', 'staff_view']
    see_from_listB  = ['student_view', 'staff_view']

    all_main = [
            #'text'         
            #   'styling_class(es)',    
            #       'links_to'
            #           'permission_required'
            #               '[seen_from]'
            #                   'selected'
            ['Coaches', 
                '',  
                    reverse('course_select'),
                        'any',
                            see_from_listA,
                                'coaches',

            ],
            ['Student View', 
                '',  
                    reverse('mycoach:message_view', kwargs={'msg_id' : ''}),
                        'staff',
                            see_from_listB,
                                'student_view',
            ],
            ['Staff View', 
                '',  
                    reverse('mystaff:default'),
                        'staff',
                            see_from_listB,
                                'staff_view',

            ],
            [''.join(['Logout: ', user.username]),      
                '', 
                    reverse('mylogout'),
                        'any',
                            see_from_listA,
                                'never',


            ]
        ]

    main_nav = []
    for nn in all_main:
        # style the selected option
        if nn[5] == selected:
            nn[1] = 'current'
        # sceen from this page type?
        if selected in nn[4]:
            # permission?
            if nn[3] == 'any':
                main_nav.append(nn)
            elif nn[3] == 'staff' and user.is_staff:
                main_nav.append(nn)

    return main_nav


def tasks_nav(user, selected):
    
    all_tasks = [
            #'text'         
            #   'styling_class(es)',    
            #       'links_to'
            #           'permission_required'
            #               'selected'
            ['Publisher', 
                '',  
                    reverse('mypublisher:checkout'),
                        'staff',
                            'review',

            ]
        ]
    """
    ,
                ['Data Loader', 
                    '',  
                        reverse('myloader:upload_files'),
                            'staff',
                                'upload_files',

                ],
                ['Emailer', 
                    '',  
                        reverse('mypublisher:create_bcc'),
                            'staff',
                                'create_bcc',

                ]
    """
    tasks_nav = []
    for nn in all_tasks:
        # style the selected option
        if nn[4] == selected:
            nn[1] = 'current'
        # permission?
        if nn[3] == 'any':
            tasks_nav.append(nn)
        elif nn[3] == 'staff' and user.is_staff:
            tasks_nav.append(nn)

    return tasks_nav
