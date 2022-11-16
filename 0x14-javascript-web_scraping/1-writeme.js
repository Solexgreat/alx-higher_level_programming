#!/usr/bin/node

const fs = require('fs');
const body = process.argv[3];
fs.writeFileSync(process.argv[2],  process.argv[3])
