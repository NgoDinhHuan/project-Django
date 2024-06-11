function gotoCart(pid){
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
	$.ajax({
	    url: '/postgiohang/',
	    contentType: 'application/json',
		type: 'post',
		headers:{
        "X-CSRFToken": csrftoken
        },
		data: pid,
		success: function(response){
			var data = response;
			console.log(data)
			if (data =='0' && pid != '0'){
			     alert('Bạn cần đăng nhập mới có thể mua hàng');
			}
			else if (pid != '0' && data !='0 '){
		    alert('Đã Thêm Vào Giỏ Hàng');
//			    document.getElementById("alert_giohang").innerHTML = '<div class="alert alert-success"><i class="fa fa-check-circle"></i>Đã Thêm Vào giỏ Hàng</div>';
			}

        $("#cart-item").html(data);
		}
	});
}