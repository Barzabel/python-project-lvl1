### Hexlet tests and linter status:
![Actions Status](https://github.com/Barzabel/python-project-lvl1/workflows/hexlet-check/badge.svg)

<div>
<button type="submit" id="down">назад</button>	
<button type="submit" id="up">вперед</button>	
</div>

{% block javascript %}
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

  <script>
	$(document).ready(function () 
	{

		var page = 1 // НЕ МОЖЕТ БЫТЬ МЕНЬШЕ ОДНОГО ЭТО ГЕТ ПАРАМЕТОР ДЛЯ API

		function get_list_car(page)
		{
			$.ajax(
			{
				type: "get",
					data: {"page": page ,}, // отправляем данные на сервер
					url: "{% url 'api_list_car' %}",

				success:function(data)
				{
					var car_list = document.getElementById("car_list") // ЗАПОЛНЯЕМ DIV ДАННЫМИ С СЕРВЕРА
					car_list.textContent = ""
					var h = document.createElement('h2');
					h.textContent = 'страничка №' + page;
					car_list.append( h )					

					var hr = document.createElement('hr');
					car_list.append( hr )		

					for (var i = 0; i < data.length; i++) 
					{
						var p = document.createElement('p');
						p.textContent = (i+1) + '. ' + data[i].brand+ ' '+ data[i].enterprise + ' '  + data[i].code;
						car_list.append( p )
   					}
				}
	    	});
	    }

	    get_list_car(page); //вызываем функцию для старта


		document.querySelector("#up").onclick = function()
		{
			page++;
			get_list_car(page);
			
		}

		document.querySelector("#down").onclick = function()
		{
			if (page > 1){
				page--;
			}
			get_list_car(page)
		}

		return false;
  })

  </script>
{% endblock javascript %}
