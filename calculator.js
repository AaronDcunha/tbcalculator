

//START OF THE MATRIX CODE!!!!!!
function startMatrix(){
	

	
	const _row1 = [];
	const _row2 = [];
	const _row3 = [];
	
	_row1.push(document.getElementById("r11").value);
	_row1.push(document.getElementById("r12").value);
	_row1.push(document.getElementById("r13").value);
	_row1.push(document.getElementById("r14").value);
	
	_row2.push(document.getElementById("r21").value);
	_row2.push(document.getElementById("r22").value);
	_row2.push(document.getElementById("r23").value);
	_row2.push(document.getElementById("r24").value);
	
	_row3.push(document.getElementById("r31").value);
	_row3.push(document.getElementById("r32").value);
	_row3.push(document.getElementById("r33").value);
	_row3.push(document.getElementById("r34").value);
	
	
	solveMatrix(_row1,_row2,_row3);
	
}


//Function compute GCD
function gcd(x,y){
	

    
  x = Math.abs(x);
  y = Math.abs(y);
  while(y) {
    var t = y;
    y = x % y;
    x = t;
  }
  return x;
	
}

function compute_lcm(x,y){
	
	let lcm = Math.floor( (x*y) / gcd(x,y));

	return lcm;
	
}

function add(row1,row2){
	
	let r1 = row1.slice(0,row1.length);
	let r2 = row2.slice(0,row2.length);
	
	for(let i=0; i< r1.length;i++){
		
		r2[i] = Number(r2[i]) + Number(r1[i]);
		
	}
	
	return r2;
	
}

function multiplyrow(row1,val){
	console.log(row1)
	let r1 = row1.slice(0,row1.length);
	
	
	
	for(let i=0; i< r1.length;i++){
		console.log(r1[i]);
		console.log(val);
		r1[i] = Number(r1[i]) * Number(val);
		if(isNaN(r1[i])){
			console.log(r1[i]);
			throw "NOT POSSIBLE"
		}
		
	}
	
	return r1;
	
}

function printMatrix(r1,r2,r3){
	
	var mx = "";
	
	mx = mx + "[";
	
	for(let i = 0; i < r1.length-1;i++){
		mx = mx+r1[i] + ",";
	}
	mx = mx+" | " + r1[3] + "]";
	mx = mx+"<br/>";
	
	mx = mx + "[";
	
	for(let i = 0; i < r2.length-1;i++){
		mx = mx+r2[i] + ",";
	}
	mx = mx+" | " + r2[3] + "]";
	mx = mx+"<br/>";
	
	mx = mx + "[";
	
	for(let i = 0; i < r3.length-1;i++){
		mx = mx+r3[i] + ",";
	}
	mx = mx+" | " + r3[3] + "]";
	mx = mx+"<br/>";
	
	
	return mx;
	
}





function solveMatrix(r1,r2,r3){
	
	const steps = [];

	try{
				
		steps.push("Given Matrix:");
		steps.push(printMatrix(r1,r2,r3));
		
		//Step1
		console.log(r3[0] != 0);
		if(r3[0]!=0){
			
			if(compute_lcm(r1[0],r3[0]) < compute_lcm(r2[0],r3[0])){
                
                var lcm = compute_lcm(r1[0],r3[0]);
				console.log(lcm)
                var r3mul =  lcm/r3[0] ;
                var r1mul =  lcm/r1[0] ;
                
                if( (r1[0] * r1mul ) / (r3[0] * r3mul) == 1 ){
                    r3mul = r3mul* (-1);
				}   
                const tempR1=multiplyrow(r1, r1mul)
                const tempR3=multiplyrow(r3,r3mul)
                r3 = add(tempR1,tempR3)
                
                steps.push(r1mul+"R1 " +"+ " + r3mul + "R3 => R3")
				console.log(r1,r2,r3);
			}  
            else{
                
                var lcm = compute_lcm(r2[0],r3[0]);
				console.log(lcm)
                var r3mul =  lcm / r3[0];
                var r2mul =  lcm /r2[0] ;
                
                if( (r2[0] * r2mul ) / (r3[0] * r3mul) == 1 ){
                    r3mul = r3mul* (-1);
				}  
                const tempR2=multiplyrow(r2, r2mul);
                const tempR3=multiplyrow(r3,r3mul);
                r3 = add(tempR2,tempR3);
                
				steps.push(r2mul+"R2 " +"+ " + r3mul + "R3 => R3");
                
				
				
           
			}
				
			 steps.push(printMatrix(r1,r2,r3));
		}
		
		//Step2
		 if(r2[0] != 0){
          
            lcm = compute_lcm(r1[0],r2[0]);
            r2mul =  lcm/r2[0] ;
            r1mul =  lcm/r1[0] ;
            
            if( (r1[0] * r1mul ) / (r2[0] * r2mul) == 1 ){
				
                r2mul *= -1;
			}
            tempR1=multiplyrow(r1, r1mul);
            tempR2=multiplyrow(r2,r2mul);
            r2 = add(tempR1,tempR2);
            
          
			steps.push(r1mul+"R1 " +"+ " + r2mul + "R2 => R2");
                
            
                
            steps.push(printMatrix(r1,r2,r3));
		 }
		 
		 //Step2.5
		 if(r2[1] == 0){
          
            r3copy = r3.slice(0,r3.length);
			r2copy = r2.slice(0,r2.length);
            
			r2 = r3copy;
			r3 = r2copy;
			steps.push("Invert R2 and R3");
                
            
                
            steps.push(printMatrix(r1,r2,r3));
		 }
		 
		 //Step3
		 if(r3[1] != 0){
          
            lcm = compute_lcm(r2[1],r3[1]);
			console.log("LCM IS " + lcm);
			console.log(r2[1],r3[1]);
            r2mul =  lcm/r2[1] ;
            r3mul =  lcm/r3[1] ;
            
            if( (r3[1] * r3mul ) / (r2[1] * r2mul) == 1 ){
                r2mul *= -1;
			}
                
            tempR3=multiplyrow(r3, r3mul);
            tempR2=multiplyrow(r2,r2mul);
            r3 = add(tempR2,tempR3);
            
         
            steps.push(r2mul+"R2 " +"+ " + r3mul + "R3 => R3");    
            
                
            steps.push(printMatrix(r1,r2,r3));
		
		 }
		 
		 //Step4
		 if(r3[2] != 1){
            
			steps.push("1/" +r3[2] + " R3 => R3");  
			
            r3 = multiplyrow(r3,1/r3[2]);

            steps.push(printMatrix(r1,r2,r3));
		 }
		 
		 //Step5
		 if(r2[2] != 0){
            tempr3 = multiplyrow(r3,-r2[2]);
			steps.push(-r2[2]+"R3 " +"+ " + 1 + "R2 => R2");   
            r2 = add(tempr3,r2);
            steps.push(printMatrix(r1,r2,r3));
		 }
		 
		 //Step6
		 if(r2[1] != 1){
			steps.push("1/" +r2[1] + " R2 => R2");
            r2 = multiplyrow(r2,1/r2[1]);
            steps.push(printMatrix(r1,r2,r3));
		 }
		 
		 //Step7
		 if(r1[1] != 0){
			console.log(printMatrix(r1,r2,r3));
            tempr2 = multiplyrow(r2,-r1[1])
			steps.push(-r1[1]+"R2 " +"+ " + 1 + "R1 => R1");  
			console.log(printMatrix(r1,r2,r3));
            r1 = add(r1,tempr2);
			
            steps.push(printMatrix(r1,r2,r3));
		 }
		 
		 //Step8
		 if(r1[2] != 0){
			 console.log(printMatrix(r1,r2,r3));
            tempr3 = multiplyrow(r3,-r1[2])
			steps.push(-r1[2]+"R3 " +"+ " + 1 + "R1 => R1");  
            r1 = add(r1,tempr3)
			console.log(printMatrix(r1,r2,r3));
            steps.push(printMatrix(r1,r2,r3));
		 }
		 
		 //Step9
		 if(r1[0] != 1){
           
			steps.push("1/" +r1[0] + " R1 => R1");
            r1 = multiplyrow(r1,1/r1[0]);
            steps.push(printMatrix(r1,r2,r3));
		 }
		 
		 steps.push("Therefore solution: "+ "("+r1[3]+","+r2[3]+","+r3[3]+")")
		
		var stepText = "";
		document.getElementById("GaussianSpan").innerHTML = "";
		for(let i = 0; i < steps.length; i++){

			stepText = stepText + "<br/>" + "<br/>" + steps[i];
			
		}
		
		document.getElementById("GaussianSpan").innerHTML = stepText;
		
	}catch (error){
	
	console.log(error)
		document.getElementById("GaussianSpan").innerHTML = "No solution possible from given matrix (OR) error in inputs." 
		
	}
	
	
	
}




