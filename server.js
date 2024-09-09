const express = require('express');
const multer = require('multer');
const cors = require('cors');
const path = require('path');
const { spawn } = require('child_process');
const fs = require('fs');

const app = express();
app.use(cors());
app.use(express.json());

const upload = multer({ dest: 'uploads/' });

app.post('/api/upload', upload.single('video'), (req, res) => {
  const videoPath = req.file.path;
  
  // Call Python script to process the video
  const pythonProcess = spawn('python', ['generatehighlights.py', videoPath]);

  pythonProcess.stdout.on('data', (data) => {
    const outputPath = data.toString().trim();
    res.json({ highlightUrl: `http://localhost:5000/${outputPath}` });
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`Error: ${data}`);
    res.status(500).send('Error processing video');
  });
});

// Serve static files (processed videos)
app.use('/highlights', express.static(path.join(__dirname, 'highlights')));

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
