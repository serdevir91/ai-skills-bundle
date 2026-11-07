# AI Skills Bundle

Claude Code, Codex ve benzeri ajanlar için skill ve kural paketi. API anahtarı, hesap kimliği ve özel bilgi içermez.

## Hızlı kurulum

Yapay zekana şunu yaz:

```text
https://raw.githubusercontent.com/serdevir91/ai-skills-bundle/main/INSTALL.md
Bu dosyadaki talimatlarla skilleri kur.
```

Elle kurulum:

```bash
git clone --depth 1 https://github.com/serdevir91/ai-skills-bundle.git
cd ai-skills-bundle
./install.sh --list
./install.sh custom workflow
```

Varsayılan hedef `~/.claude/skills`. Başka klasör için `--target DIR` kullan. Sadece kullanacağın skill'leri kur, hepsini kurmak bağlamı doldurur.

## İçerik

| Klasör | Ne var |
|---|---|
| `skills/custom/` | Store yayını, Flutter baseline ve audit, ajan delegasyonu, scraping, reverse engineering |
| `skills/workflow/` | Kısa yanıt, dikkatli kodlama, inceleme ve doğrulama akışları |
| `skills/firebase/` | Firebase, Firestore ve Xcode kurulumu |
| `skills/anthropic/` | Tasarım, doküman, MCP ve test skill'leri |
| `skills/community/` | Mühendislik, ürün, pazarlama ve uyum rol skill'leri |
| `rules/` | Örnek `AGENTS.md` ve `CLAUDE.md` kuralları |
| `scripts/` | iOS Simulator boşta kapatma hook'ları |

`<ISSUER_ID>`, `<KEY_ID>`, `<WORKSPACE>`, `com.example.myapp` gibi değerler placeholder. Kendi değerlerini kullan.

## Pakette olmayanlar

- Anthropic `docx`, `pdf`, `pptx`, `xlsx`: Lisansları yeniden dağıtıma izin vermiyor. Kaynak: https://github.com/anthropics/skills
- `upload_to_*.py` store scriptleri ve kişisel notlar.

## Ayrıca kurulacaklar

- Eklentiler: `JuliusBrussee/caveman`, `Creatorberry/flick`
- Delegasyon için CLI: Antigravity (`agy`), OpenCode (`opencode`)
- Scraping için: `scrapling`

## Kaynak ve lisans

Üçüncü taraf içerik kendi lisansıyla gelir, lisans dosyaları ilgili klasörlerdedir.

- Anthropic: Apache-2.0, https://github.com/anthropics/skills
- Community: MIT, https://github.com/alirezarezvani/claude-skills
- Caveman: Apache-2.0 / MIT, https://github.com/JuliusBrussee/caveman
- Firebase: Apache-2.0, https://github.com/firebase/agent-skills
- Scrapling: `skills/custom/scrapling-official/LICENSE.txt`, https://github.com/D4Vinci/Scrapling
