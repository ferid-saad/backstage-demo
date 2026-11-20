const express = require('express');
const app = express();
const PORT = process.env.PORT || 3001;

app.get('/health', (req, res) => {
  res.json({ status: 'ok', service: '${{ values.repoName }}' });
});

app.listen(PORT, () => {
  console.log(`${{ values.repoName }} running on port ${PORT}`);
});
