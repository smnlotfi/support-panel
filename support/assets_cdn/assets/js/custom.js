function get_all_user(e){
    e.preventDefault()
    $.ajax({
      type:'POST',
      url:'users',
      data:{'get_users':'true'},
      dataType:'json',
      success:function(res){
          alert(res)
      },
      error:function(){
        alert('error')
      }

    })
  }


  function add_user(e){
    e.preventDefault()
    $.ajax({
      type:'POST',
      url:'users',
      data:$('#add_user').serialize(),
      dataType:'json',
      success:function(res){
        alert(res.msg)
        get_all_user(e)
      },
      error:function(){
        alert('error')
      }

    })
  }

  
  $('#add_user').submit(function(e){
    add_user(e)
  })