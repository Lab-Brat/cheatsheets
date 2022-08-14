## CSS basics

### selectors
* tag
```css
p {
  color: red;
}
```

* id
```css
#id1 {
  background_color: red;
}
```

* class
```css
.class1 p {
  color: red;
}
```

* class detail
```css
.class1 dev p {
  color: red;
}
```

### block / inline
display: block  
display: inline  
display: inline-block  
display: none  

### sizing
```css
html {
  height: 100%;
}

body {
  height: 50%;
  width: 50%;
  margin: 0;
}

.class1 {
  height: 100vh; # size of the viewport
  width: 50px;   # static size
}
```


### box model
content  
padding  
border  
margin  
```css
.class1 {
  background-color: antiquewhite;
  padding: 5px 10px 5px 10px;  # top rign bottom left
  border: 1px solid black;
  margin: 1px; 
}
```
