#!/usr/bin/node
const first_arg = require('fs');

const first_Arg = first_arg.readFileSync(process.argv[2]).toString();
const second_Arg = first_arg.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], first_Arg + second_Arg);
