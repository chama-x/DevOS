#!/usr/bin/env node

/**
 * create-groundrules.js — Set boundaries for your AI coding agent in 5 seconds.
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
  console.log('\n🎯 GroundRules — Set boundaries for your AI coding agent in 5 seconds.\n');

  const stack = await ask('1. Tech stack (e.g. Next.js 15, Supabase): ');
  const neverDo = await ask('2. What is the ONE thing the agent must NEVER do? (e.g. Never touch auth logic): ');
  const testCmd = await ask('3. Test command (e.g. npm test): ');

  rl.close();

  const templateDir = path.join(__dirname, '..', 'template');
  if (!fs.existsSync(templateDir)) {
    console.error('Error: template directory not found at', templateDir);
    process.exit(1);
  }

  fs.cpSync(templateDir, process.cwd(), { recursive: true });

  const identityPath = path.join(process.cwd(), '.agents', 'rules', 'IDENTITY.md');
  if (fs.existsSync(identityPath)) {
    let identity = fs.readFileSync(identityPath, 'utf8');
    identity = identity.replace('[e.g., Next.js 15, Supabase, Tailwind v4]', stack || 'Node.js');
    identity = identity.replace('`[e.g., npm run test]`', `\`${testCmd || 'npm test'}\``);
    identity = identity.replace('- [e.g., Never touch auth logic without approval]', `- ${neverDo || 'Never make unapproved breaking changes'}`);
    fs.writeFileSync(identityPath, identity);
  }

  console.log('\n✅ GroundRules initialized.');
  console.log('   Rules set in .agents/rules/IDENTITY.md & GROUNDING.md\n');
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
