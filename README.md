# Ven-Task-Manager
Ven Task Manager

## Methods

### `ven init` 
Starts ven task manager    
1.  Check if ven.json already exists in current folder
    *  *Error message* if already exists
2.  Ask config questions
    *  user name
    *  user email
    *  money per hour (optional)
3.  Creates `ven.json` file

## Data 

### `ven.json` structure

    {
        'username': ...string ,
        'useremail': ...string ,
        'days' [
            '*task_id*': {
                'isCompleted': *true/false*,
                'time': [*begin_time*, *pause_time*, ...dataTime ],
                'description': ...string
            },
            ...dict
        ],
        'money': ...0.2float
    }

## TODO 

### Functionalities

#### :x: Create the best way to validate args
#### :x: Create `ven_installer.exe`
#### :x: Create `ven.exe`
`ven.py` code recompiled to `ven.exe`
#### :x: Association with `git`

### Methods

|    Methods    |    Progress   |     Docs      |
|  :---------:  |  :---------:  |  :---------:  |
|  init         | `[_________]` | `[#########]` |
|  username     | `not started` | `not started` |
|  useremail    | `not started` | `not started` |
|  start        | `not started` | `not started` |
|  finish       | `not started` | `not started` |
|  run          | `not started` | `not started` |
|  pause        | `not started` | `not started` |
|  switch       | `not started` | `not started` |
|  today        | `not started` | `not started` |
|  status       | `not started` | `not started` |
|  export       | `not started` | `not started` |


### ven init

Creates ven file that stores everything

### ven start

Starts a new task

Opens console to fill task data 

Task data should be made by a configurable file that can be of any type

### ven finish 

Finishes current task

### ven run

Resumes count of some task

### ven pause

Pauses count of some task

### ven switch

Switch to another task / creates new task and switch to (maybe could be a parameter)



