Interpretation: On clicking submit button
- Hit the api "/removepunc/" with params "text: {{text}}"

```
<form action='/removepunc/' method='get'>
        <textarea name='text' style='width: 470px; height: 350px;'></textarea>
        <br>
        <button type='submit'>Analyze Text</button>
</form>
```
- `<p>` tag doesn't retain new line characters
- `<pre>` tag is used to retain new line characters
