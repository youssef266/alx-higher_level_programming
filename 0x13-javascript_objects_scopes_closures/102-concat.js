#!/usr/bin/node
const frist_arg = require('fs');

const first_Arg = frist_arg.readFileSync(process.argv[2]).toString();
const secound_Arg = frist_arg.readFileSync(process.argv[3]).toString();
frist_arg.writeFileSync(process.argv[4], first_Arg + secound_Arg);
