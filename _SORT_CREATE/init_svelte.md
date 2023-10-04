```
<script>
	let m = { x: 0, y: 0 };
</script>

<div 
	on:pointermove={ (e) => {
		m = { x: e.clientX, y: e.clientY };
	}}
>
	The mouse position is {m.x} x {m.y}
</div>

<style>
	div {
		position: fixed;
		left: 0;
		top: 0;
		width: 100%;
		height: 100%;
		padding: 1rem;
	}
</style>
```
BOTH CODES DO THE SAME THING: Above=Inline Below=InScript

```
<script>
	let m = { x: 0, y: 0 };

	function handleMove(event) {
		m.x = event.clientX;
		m.y = event.clientY;
	}
</script>

<div on:pointermove={handleMove}>
	The pointer is at {m.x} x {m.y}
</div>

<style>
	div {
		position: fixed;
		left: 0;
		top: 0;
		width: 100%;
		height: 100%;
		padding: 1rem;
	}
</style>
```

---
# THINGS BEFORE
## Check necessary tech:
- npm -v
- node - v

- What this means: 
`Warning! Svelte doesn't perform any sanitization of the expression inside {@html ...} before it gets inserted into the DOM. This isn't an issue if the content is something you trust like an article you wrote yourself. However if it's some untrusted user content, e.g. a comment on an article, then it's critical that you manually escape it, otherwise you risk exposing your users to Cross-Site Scripting (XSS) attacks.`
  - inserting HTML elements in a string is possible, but safe if you trust that element
  - e.g. Inserting html template for a blog article that you created
    ```
    <script>
      let string = `this string contains some <strong>HTML!!!</strong>`;
      let blueParagraph = `this is a <strong style="color: blue">blue paragraph</strong>`
    </script>

    <p>{@html string}</p>
    <p>{@html blueParagraph}</p>
    ```



