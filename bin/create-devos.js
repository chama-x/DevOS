#!/usr/bin/env node

/**
 * create-devos.js — DevOS Interactive CLI Installer
 * Usage: node bin/create-devos.js
 */

const readline = require('readline');
const fs = require('fs');
const path = require('path');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function ask(question) {
  return new Promise((resolve) => rl.question(question, resolve));
}

async function main() {
  console.log('\n🤖 DevOS Installer — Setting project boundaries for your agent.\n');

  const stack = await ask('1. What is the primary framework/stack? (e.g., Next.js + Supabase): ');
  const neverDo = await ask('2. What is the ONE thing the agent should NEVER do? (e.g., Never touch auth logic without approval): ');
  const testCmd = await ask('3. What is the test command? (e.g., npm run test): ');

  rl.close();

  // Build directory structure by copying the template
  const templateDir = path.join(__dirname, '..', 'template');
  
  if (!fs.existsSync(templateDir)) {
    console.error('Error: template directory not found at', templateDir);
    process.exit(1);
  }

  // Copy all files from template to current directory
  fs.cpSync(templateDir, process.cwd(), { recursive: true });

  // Update IDENTITY.md with user's answers
  const identityPath = path.join(process.cwd(), '.agents', 'rules', 'IDENTITY.md');
  if (fs.existsSync(identityPath)) {
    let identity = fs.readFileSync(identityPath, 'utf8');
    identity = identity.replace('[e.g., Next.js, Node, Supabase]', stack);
    identity = identity.replace('`[e.g., npm run test]`', `\`${testCmd}\``);
    identity = identity.replace('- [e.g., Never touch auth logic without approval]', `- ${neverDo}`);
    fs.writeFileSync(identityPath, identity);
  }

  console.log('\n✅ DevOS initialized. Project boundaries set.');
  console.log('   Next: Fill in .agents/rules/IDENTITY.md with your project description.\n');
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
